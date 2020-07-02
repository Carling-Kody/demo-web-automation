
def test_radio_button(py):
    py.visit('https://demoqa.com/radio-button')
    py.get('#yesRadio').click(force=True)
    assert py.get('.text-success').should().have_text('Yes')


def test_impressive_radio_button_is_selected(py):
    py.visit('https://demoqa.com/radio-button')
    checkbox = py.get('#impressiveRadio')
    checkbox.click(force=True)
    assert checkbox.is_selected()


def test_inject_javascript_to_enable_no_radio_button(py):
    py.visit('https://demoqa.com/radio-button')
    no_radio = py.get('#noRadio')
    py.execute_script('arguments[0].disable = false', no_radio.webelement)
    py.wait(use_py=True).sleep(3)
    no_radio.click(force=True)
    assert no_radio.is_selected()