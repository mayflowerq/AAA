import csv


def get_data():
    with open('Corp_summary.csv', 'r', encoding="utf-8") as f:
        data = f.readlines()
    data = [i.strip().split(';') for i in data[1:]]
    return data


def get_hierarchy():
    """иерархия"""
    data = get_data()
    unique_departments = []
    unique_departments_and_all_teams = []
    for i in data:
        if i[1] not in unique_departments:
            unique_departments.append(i[1])
    for i in unique_departments:
        for q in data:
            if q[1] == i and q[2] not in unique_departments_and_all_teams:
                unique_departments_and_all_teams.append(i)
                unique_departments_and_all_teams.append(q[2])
    for q in unique_departments:
        print('Департамент', q, 'содержит следующие команды:')
        for i, _ in enumerate(unique_departments_and_all_teams):
            if unique_departments_and_all_teams[i] == q:
                print('    ', unique_departments_and_all_teams[i+1])


def get_report():
    """генерирует отчет"""
    data = get_data()
    final_list = []
    final_data = []
    unique_departments = []
    departments_and_salaries = []
    unique_departments_and_salaries = []
    departments_numbers = []
    for i in data:
        if i[1] not in unique_departments:
            unique_departments.append(i[1])
    for i in unique_departments:
        for q in data:
            if q[1] == i:
                departments_and_salaries.append(i)
                departments_and_salaries.append(q[5])
    for i in unique_departments:
        unique_departments_and_salaries.append(i)
        for q, _ in enumerate(departments_and_salaries):
            if i == departments_and_salaries[q]:
                unique_departments_and_salaries.append(departments_and_salaries[q + 1])
    for i, _ in enumerate(unique_departments_and_salaries):
        if unique_departments_and_salaries[i] in unique_departments:
            departments_numbers.append(i)
    for i, _ in enumerate(departments_numbers):
        counter = []
        final_list.append(unique_departments_and_salaries[(departments_numbers[i])])
        if i != len(departments_numbers) - 1:
            for q in range(departments_numbers[i] + 1, departments_numbers[i + 1]):
                counter.append(int(unique_departments_and_salaries[q]))
        else:
            for q in range(departments_numbers[i] + 1, len(unique_departments_and_salaries)):
                counter.append(int(unique_departments_and_salaries[q]))
        final_list.append(len(counter))
        final_list.append(min(counter))
        final_list.append(max(counter))
        final_list.append(round(sum(counter) / len(counter), 2))
    mydata = [["Департамент", "Численность", "МИН. З/П", "МАКС. З/П", "СРЕДН. З/П"]]
    for i, _ in enumerate(final_list):
        if final_list[i] in unique_departments:
            final_data.append(final_list[i])
            final_data.append(final_list[i + 1])
            final_data.append(final_list[i + 2])
            final_data.append(final_list[i + 3])
            final_data.append(final_list[i + 4])
            mydata.append(final_data)
            final_data = []
    return mydata


def print_report():
    """выводит отчет"""
    mydata = get_report()
    print('ОТЧЕТ ПО ДЕПАРТАМЕНТАМ:')
    for i in range(1, len(mydata)):
        print(f'    Департамент {mydata[i][0]}:')
        print(f'        Численность - {mydata[i][1]} чел., МИН. З/П - {mydata[i][2]} руб., '
              f'МАКС. З/П - {mydata[i][3]} руб., СРЕДН. З/П - {mydata[i][4]} руб.')


def write():
    """запись в csv"""
    mydata = get_report()
    myfile = open('New_file.csv', 'w', newline="")
    with myfile:
        writer = csv.writer(myfile)
        writer.writerows(mydata)
    with open('New_file.csv', 'r') as f:
        data = f.readlines()
    data = [i.strip().split(';') for i in data]
    print(data)


def main():
    a = input()
    if a == '1':
        get_hierarchy()
    elif a == '2':
        print_report()
        pass
    elif a == '3':
        write()
    else:
        print('Выберите цифру от 1 до 3')


if __name__ == '__main__':
    main()
