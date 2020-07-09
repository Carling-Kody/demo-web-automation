from pylenium import Pylenium


class Checkboxes:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_checkbox(self):
        self.py.visit('https://demoqa.com/checkbox')

    def expand_first_toggle(self):
        self.py.get("button[title='Toggle']").click()

    def expand_all(self):
        self.expand_first_toggle()
        self.expand_carrot_toggles(2)
        self.expand_carrot_toggles(3)
        self.expand_carrot_toggles(4)
        self.expand_carrot_toggles(5)
        self.expand_carrot_toggles(6)

    def close_all(self):
        self.py.get("button[title='Toggle']").click()

    def expand_carrot_toggles(self, index):
        self.py.getx(f"(//button[@title='Toggle'])[{index}]").click()

    def check_checkbox(self, index):
        self.py.getx(f"(//span[@class ='rct-checkbox'])[{index}]").click()

    def check_for_checked_status(self, index):
        """can check for "uncheck", "half-checked" or "icon-check" """
        return self.py.getx(f"(//span[@class ='rct-checkbox'])[{index}]").get_attribute('innerHTML')




