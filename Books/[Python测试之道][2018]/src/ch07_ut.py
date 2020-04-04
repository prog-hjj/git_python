import unittest
import requests
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://www.xxx.com/login.html"

    def testLogin1(self):
        # form = {"username": 13111111111, "password": 123456}
        # r = requests.post(self.url, data=form)
        # self.assertEqual(r.text, "登录成功")
        self.assertEqual("abc", "abc")

    def testLogin2(self):
        # form = {"username": "", "password": 123456}
        # r = requests.post(self.url, data=form)
        # self.assertEqual(r.text, "用户名不能为空")
        self.assertEqual("abc", 123)

    def testLogin3(self):
        # form = {"username": 13111111111, "password": ""}
        # r = requests.post(self.url, data=form)
        # self.assertEqual(r.text, "密码不能为空")
        self.assertEqual("abc", "123")

    def testLogin4(self):
        # form = {"username": 13111111111, "password": 111111}
        # r = requests.post(self.url, data=form)
        # self.assertEqual(r.text, "账号或者密码错误")
        self.assertEqual(123, 123)

class LogoutTest(unittest.TestCase):
    def testLogout(self):
        pass

def suite():
    loginTestSuite = unittest.makeSuite(LoginTest, "test")
    logoutTestSuite = unittest.makeSuite(LogoutTest, "test")
    allsuite = unittest.TestSuite((loginTestSuite, logoutTestSuite))
    return allsuite

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
    import HTMLTestRunner
    fr = open("res1.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr, title="测试报告",
                                           description="详情")
    runner.run(suite())
    fr.close()
