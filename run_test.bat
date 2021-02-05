pytest --reruns 2 --alluredir reports\allure-results --clean-alluredir
allure generate report\allure-results -c -o reports\allure-report
