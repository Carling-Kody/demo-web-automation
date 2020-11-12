import pytest

from widgets.pages.widgets_page_wrapper import WidgetPages


@pytest.fixture
def widgets(py):
    return WidgetPages(py)
