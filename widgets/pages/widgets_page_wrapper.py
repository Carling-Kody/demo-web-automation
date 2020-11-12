from pylenium import Pylenium

from widgets.pages.accordian_page import Accordian
from widgets.pages.menu_page import Menu
from widgets.pages.progress_bar_page import ProgressBar
from widgets.pages.select_menu_page import SelectMenu
from widgets.pages.slider_page import Slider


class WidgetPages:
    def __init__(self, py: Pylenium):
        self.accordian = Accordian(py)
        self.menu = Menu(py)
        self.progress_bar = ProgressBar(py)
        self.select_menu = SelectMenu(py)
        self.slider = Slider(py)
