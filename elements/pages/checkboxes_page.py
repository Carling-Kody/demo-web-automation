from pylenium import Pylenium


class Checkboxes:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_checkbox(self):
        self.py.visit('https://demoqa.com/checkbox')

    def expand_all_button(self):
        self.py.get("button[class='rct-option rct-option-expand-all']").click()

    def collapse_all_button(self):
        self.py.get("button[class='rct-option rct-option-collapse-all']").click()

    def get_checkbox_titles(self):
        labels = []
        title = self.py.find("span[class ='rct-title']")
        count = 0
        for i in title:
            labels.append(i.text().lower())
        return labels

    def create_checkbox_json(self):
        label_list = self.get_checkbox_titles()
        checkbox_dictionary = {}
        count = 0
        for item in label_list:
            checkbox_dictionary[f"{item}"] = count
            count += 1
        return checkbox_dictionary

    def expand_first_toggle(self):
        self.py.get("button[title='Toggle']").click()

    def close_all(self):
        self.py.get("button[title='Toggle']").click()

    def expand_carrot_toggles(self, index):
        self.py.getx(f"(//button[@title='Toggle'])[{index}]").click()

    def check_checkbox(self, index):
        self.py.getx(f"(//span[@class ='rct-checkbox'])[{index}]").click()

    def check_for_checked_status(self, index):
        """can check for "uncheck", "half-checked" or "icon-check" """
        return self.py.getx(f"(//span[@class ='rct-checkbox'])[{index}]").get_attribute('innerHTML')

    def check_success_message(self, name):
        return self.py.getx(f"//span[contains(text(),'{name}')]").get_attribute('outerText')




