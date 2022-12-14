Шаги для запуска:
1) скачать what_is_year_now.py, test_what_is_year_now_unit.py, поместить их в одну директорию
2) для проведения mock-тестов ввести в консоль python -m unittest -v test_what_is_year_now_unit.py
3) для проверки покрытия кода тестами ввести в консоль python -m pytest -q test_what_is_year_now_unit.py --cov=what_is_year_now
4) для создания html отчета ввести в консоль python -m pytest --cov  .  --cov-report html
