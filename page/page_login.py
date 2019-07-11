from base.base import Base


class PageLogin(Base):
    #  点击登录链接
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.login_usernamr,username)

    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd )

    #  输入验证码
    def page_input_code(self,code):
        self.base_input(page.login_code, code)

    # 点击登录链接
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    #  获取异常提示信息
    def page_get_error(self):
        return self.base_get_text(page.login_err)

    #   点击异常提示信息框确定按钮
    def page_click_err_ok_btn(self):
        self.base_click(page.login_err)


    #  获取登录后的昵称
    def page_get_nickname(self):
        pass

    #  点击安全退出
    def page_click_logout(self):
        pass

    #  组合业务方法
