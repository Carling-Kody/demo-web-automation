from typing import List

from pylenium import Pylenium
from pylenium.element import Element

from elements.models.user import User


class WebTable:

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
    SEARCH_BOX = "#searchBox"

    # Actions

    table_headers = {
        'First Name': 1,
        'Last Name': 2,
        'Age': 3,
        'Email': 4,
        'Salary': 5,
        'Department': 6
    }

    def go_to_web_table_page(self) -> 'WebTable':
        self.py.visit('https://demoqa.com/webtables')
        return self

    def get_column_cells_by_name(self, column_name) -> List[Element]:
        header = self.table_headers[column_name]
        return self.py.findx(f"//div[@role='rowgroup']/div//div[{header}]")

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

    def search_for_user(self, text: str):
        self.py.get(self.SEARCH_BOX).type(text)

    def get_populated_emails(self) -> List[str]:
        """ Gets a list of all populated emails as strings """
        email_cells = self.get_column_cells_by_name('Email')
        return [cell.text() for cell in email_cells if cell.text() != ' ']


    @staticmethod
    def get_filtered_rows_by_email(rows, email) -> List[Element]:
        return [row for row in rows if email in row.text()]
    # for row in rows:
    #   if email in row.text():
    #        filtered_rows.append(row)

    def get_user_by_email(self, email) -> User:
        users = self.get_all_users()
        return next(user for user in users if user.email == email)

    def get_all_users(self) -> List[User]:
        users = list()
        rows = self.py.find("[role='rowgroup']")
        for row in rows:
            cells = self.py.find('.rt-td')
            first_name = cells[0].text()
            last_name = cells[1].text()
            age = int(cells[2].text())
            salary = int(cells[3].text())
            department = cells[4].text()
            users.append(User(first_name=first_name,
                              last_name=last_name,
                              age=age,
                              salary=salary,
                              department=department))
        return users
