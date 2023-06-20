
import pytest
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """执行并生成allure测试报告"""
    pytest.main(["-s", "-v", "--alluredir", "./report/result", "--clean-alluredir",
                 './tests/test_gwyc_api_all.py'])
    import subprocess  # 通过标准库中的subprocess包来fork一个子进程，并进行一个外部的程序

    subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)  # 读取json文件并生成html报告，
    # --clean若目录存在则先清除
    subprocess.call('allure open -h 127.0.0.1 -p 8899 ./report/html', shell=True)  # 生成一个本地的服务并自动打开html报告

