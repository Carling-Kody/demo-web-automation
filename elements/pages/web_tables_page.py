from pylenium import Pylenium


class Webtable:

    def __init__(self, py: Pylenium):
        self.py = py

    # Locators
    ADD_NEW_RECORD = "#addNewRecordButton"
    FIRST_NAME = "#firstName"
    LAST_NAME = "#lastName"
    EMAIL = "#userEmail"
    AGE = "#age"
    SALARY = "#salary"
    DEPARTMENT = "#department"
    SUBMIT_NEW_RECORD_BUTTON = "#submit"
    REGISTRATION_FORM_CLOSE = ".close"

    # Actions

    def go_to_web_table_page(self):
        self.py.visit('https://demoqa.com/webtables')

    def click_add_new_record_button(self):
        self.py.get(self.ADD_NEW_RECORD).click()

    def type_first_name(self, first_name=None):
        if first_name is None:
            test_name = self.py.fake.first_name()
            self.py.get(self.FIRST_NAME).type(test_name)
            return test_name
        else:
            self.py.get(self.FIRST_NAME).type(first_name)

    def type_last_name(self, last_name=None):
        if last_name is None:
            self.py.get(self.LAST_NAME).type(self.py.fake.last_name())
        else:
            self.py.get(self.LAST_NAME).type(last_name)

    def type_email(self, email=None):
        if email is None:
            self.py.get(self.EMAIL).type(self.py.fake.email())
        else:
            self.py.get(self.EMAIL).type(email)

    def type_age(self, age=None):
        if age is None:
            self.py.get(self.AGE).type("40")
        else:
            self.py.get(self.AGE).type(age)

    def type_salary(self, salary=None):
        if salary is None:
            self.py.get(self.SALARY).type("40000")
        else:
            self.py.get(self.SALARY).type(salary)

    def type_department(self, department=None):
        if department is None:
            self.py.get(self.DEPARTMENT).type(self.py.fake.job())
        else:
            self.py.get(self.DEPARTMENT).type(department)

    def click_submit_new_record_button(self):
        self.py.get(self.SUBMIT_NEW_RECORD_BUTTON).click()

    def add_new_record(self, first_name=None, last_name=None, email=None, age=None, salary=None, department=None):
        self.click_add_new_record_button()
        if first_name is None:
            test_name = self.type_first_name(first_name)
            self.type_last_name(last_name)
            self.type_email(email)
            self.type_age(age)
            self.type_salary(salary)
            self.type_department(department)
            self.click_submit_new_record_button()
            return test_name
        else:
            self.type_first_name(first_name)
            self.type_last_name(last_name)
            self.type_email(email)
            self.type_age(age)
            self.type_salary(salary)
            self.type_department(department)
            self.click_submit_new_record_button()




