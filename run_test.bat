pytest --reruns 2 --alluredir report\allure-results --clean-alluredir

allure generate report\allure-results -c -o report\allure-report
