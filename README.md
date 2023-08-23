# autotests_python_project
Перед запуском тестов необходимо установить зависимости из файла requirements.txt с помощью команды
pip install -r requirements.txt
Тесты с маркировкой need_review запускаются командой
pytest -v --tb=line --language=en -m need_review
Тесты на регистрацию запускаются с помощью команды
pytest -s -m "registration" test_product_page.py
Полный прогон тестов из файлов test_main_page.py и test_product_page.py можно запустить с помощью команд
pytest -s test_main_page.py
pytest -s test_product_page.py
