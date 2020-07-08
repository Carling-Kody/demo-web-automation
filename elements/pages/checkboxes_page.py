from pylenium import Pylenium


class Checkboxes:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_checkbox(self):
        self.py.visit('https://demoqa.com/checkbox')

    def expand_home_toggle_first_time(self):
        self.py.get("button[title='Toggle']").click()

    def expand_toggles(self, index):
        self.py.getx(f"(//button[@title='Toggle'])[{index}]").click()

    def check_checkbox(self, index):
        self.py.getx(f"(//span[@class ='rct-checkbox'])[{index}]").click()

    def check_for_half_checked_status(self, index):
        return self.py.getx(f"(//span[@class ='rct-checkbox'])[{index}]").get_attribute('innerHTML')


