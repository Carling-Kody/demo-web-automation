from pylenium import Pylenium


class TextBox:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa(self):
        self.py.visit('https://demoqa.com/text-box')

    def type_user_name(self, user_name):
        self.py.get("#userName").type(user_name)

    def type_user_email(self, user_email):
        self.py.get("#userEmail").type(user_email)

    def get_current_address(self):
        self.py.get("#currentAddress").type(self.py.fake.address())

    def get_permanent_address(self):
        self.py.get("#permanentAddress").type(self.py.fake.address())

    def submit_form(self):
        self.py.get("#submit").click()
