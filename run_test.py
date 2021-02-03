# -*- coding: UTF-8 -*-
import os
import subprocess

# def api_docs_path():
#     curpath = os.path.dirname(os.path.realpath(__file__))
#     api_docs_path = os.path.join(curpath, 'api_docs')
#     if not os.path.exists(api_docs_path):
#         os.mkdir(api_docs_path)
#     return api_docs_path


curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, 'report')

# file_name = 'cut_info.har'
#
# if file_name in os.listdir(filePath):
#     real_name = file_name
#     print(real_name)
#
#     dir = r"C:\ApiDocsToJson\HttpRunner"
#     cmdline = f"har2case -2j {real_name}"


cmdline_list = [
    r'pytest --reruns 2 --alluredir report\allure-results --clean-alluredir',
    r'allure generate report/allure-results -c -o report/allure-report',
    # r'allure open allure-report'
]


def rc():
    for cmdline in cmdline_list:
        # run `cmdline` in `dir`
        subprocess.run(cmdline, cwd=curpath, shell=True)
        # subprocess.Popen
        # rc = call(cmdline, cwd=curpath, shell=True)
        # print(rc)


if __name__ == '__main__':
    rc()
    # print(report_path)
