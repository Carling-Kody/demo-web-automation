from pylenium import Pylenium


class ProgressBar:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_progress_bar(self):
        self.py.visit('https://demoqa.com/progress-bar')