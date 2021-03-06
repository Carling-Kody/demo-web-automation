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
        titles = self.py.find("span[class ='rct-title']")
        for title in titles:
            labels.append(title.text().lower())
        return labels

    def checkbox_json(self):
        label_list = self.get_checkbox_titles()
        checkbox_dictionary = {}
        count = 1
        for label in label_list:
            checkbox_dictionary[f"{label}"] = count
            count += 1
        return checkbox_dictionary

    def expand_first_toggle(self):
        self.py.get("button[title='Toggle']").click()

    def expand_carrot_toggles(self, index):
        self.py.getx(f"(//button[@title='Toggle'])[{index}]").click()

    def check_checkbox(self, name):
        index = self.checkbox_json()[name]
        self.py.getx(f"(//span[@class ='rct-checkbox'])[{index}]").click()

    def check_for_checked_status(self, name):
        """can check for "uncheck", "half-checked" or "icon-check" """
        index = self.checkbox_json()[name]
        return self.py.getx(f"(//span[@class ='rct-checkbox'])[{index}]").get_attribute('innerHTML')

    def check_success_message(self, name):
        return self.py.getx(f"//span[contains(text(),'{name}')]").get_attribute('outerText')

    def get_success_messages(self):
        success_list = []
        messages = self.py.find('.text-success')

        for message in messages:
            success_list.append(message.text())

        return success_list





