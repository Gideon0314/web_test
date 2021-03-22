# -*- coding: UTF-8 -*-
import os
import subprocess
from datetime import datetime
from time import sleep
from tools.zip_file import zip_compress


def rc():

    curpath = os.path.dirname(os.path.realpath(__file__))

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    allure_result, allure_report = f"result_{now}", f"report_{now}"

    cmdline_list = [
        f'pytest --reruns 2 --alluredir reports\\{allure_result} --clean-alluredir',
        f'allure generate reports\\{allure_result} -c -o reports\\{allure_report}',
        # r'allure open allure-report'
    ]
    for cmdline in cmdline_list:

        ret = subprocess.run(cmdline, cwd=curpath, shell=True)
        if ret.returncode == 0:
            print("success:", ret)
            pass
        else:
            return ret.returncode
    sleep(5)
    zip_compress(f'reports\\{allure_report}',f'reports\\{allure_report}.zip')


if __name__ == '__main__':
    rc()
