import pytest

from elements.pages.elements_page_wrapper import ElementPages


@pytest.fixture
def elements(py):
    return ElementPages(py)
