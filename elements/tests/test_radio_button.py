
def test_radio_button(elements, py):
    elements.radio_button.go_to_demoqa_radio_button()
    py.get('#yesRadio').click(force=True)
    assert py.get('.text-success').should().have_text('Yes')  # _have_text = match
    # assert py.get('.text-success').should().contain_text('Yes')  # .contain_text = contains
    # assert py.get('.text_success').text()== 'yes' # this is the same thing as line 6


def test_impressive_radio_button_is_selected(elements, py):
    elements.radio_button.go_to_demoqa_radio_button()
    checkbox = py.get('#impressiveRadio')
    checkbox.click(force=True)
    assert checkbox.is_selected()


def test_inject_javascript_to_enable_no_radio_button(elements, py):
    elements.radio_button.go_to_demoqa_radio_button()
    no_radio = py.get('#noRadio')
    py.execute_script('arguments[0].disabled= false', no_radio.webelement)  # using Javascript to enable the button
    no_radio.click(force=True)
    assert no_radio.is_selected()