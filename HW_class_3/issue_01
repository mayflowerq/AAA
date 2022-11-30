import csv


def get_hierarchy():
    """иерархия"""
    with open('Corp_summary.csv', 'r', encoding="utf-8") as f:
        data = f.readlines()
    data = [i.strip().split(';') for i in data[1:]]
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
        for i in range(len(unique_departments_and_all_teams)):
            if unique_departments_and_all_teams[i] == q:
                print('    ', unique_departments_and_all_teams[i+1])
    return


def get_report():
    """репорт"""
    with open('Corp_summary.csv', 'r', encoding="utf-8") as f:
        data = f.readlines()
    data = [i.strip().split(';') for i in data[1:]]
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
        for q in range(len(departments_and_salaries)):
            if i == departments_and_salaries[q]:
                unique_departments_and_salaries.append(departments_and_salaries[q+1])
    for i in range(len(unique_departments_and_salaries)):
        if unique_departments_and_salaries[i] in unique_departments:
            departments_numbers.append(i)
    print('ОТЧЕТ ПО ДЕПАРТАМЕНТАМ:')
    for i in range(len(departments_numbers)):
        counter = []
        if i != len(departments_numbers)-1:
            for q in range(departments_numbers[i]+1, departments_numbers[i+1]):
                counter.append(int(unique_departments_and_salaries[q]))
        else:
            for q in range(departments_numbers[i] + 1, len(unique_departments_and_salaries)):
                counter.append(int(unique_departments_and_salaries[q]))

        print(f'    Департамент {unique_departments_and_salaries[(departments_numbers[i])]}:')
        print(f'        Численность - {len(counter)} чел., МИН. З/П - {min(counter)} руб., '
              f'МАКС. З/П - {max(counter)} руб., СРЕДН. З/П - {round(sum(counter)/len(counter), 2)} руб.')
    return


def write():
    """запись в csv"""
    with open('Corp_summary.csv', 'r', encoding="utf-8") as f:
        data = f.readlines()
    data = [i.strip().split(';') for i in data[1:]]
    unique_departments = []
    departments_and_salaries = []
    unique_departments_and_salaries = []
    departments_numbers = []
    final_list = []
    final_list_for_csv = []
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
        for q in range(len(departments_and_salaries)):
            if i == departments_and_salaries[q]:
                unique_departments_and_salaries.append(departments_and_salaries[q + 1])
    for i in range(len(unique_departments_and_salaries)):
        if unique_departments_and_salaries[i] in unique_departments:
            departments_numbers.append(i)
    for i in range(len(departments_numbers)):
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
    for i in range(len(final_list)):
        if final_list[i] in unique_departments:
            final_list_for_csv.append(final_list[i])
            final_list_for_csv.append(final_list[i+1])
            final_list_for_csv.append(final_list[i+2])
            final_list_for_csv.append(final_list[i+3])
            final_list_for_csv.append(final_list[i+4])
            mydata.append(final_list_for_csv)
            final_list_for_csv = []
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
        get_report()
        pass
    elif a == '3':
        write()
    else:
        print('Выберите цифру от 1 до 3')


if __name__ == '__main__':
    main()
