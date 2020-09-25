

def test_element_with_dynamic_id_has_text(elements, py):
    elements.dynamic_properties.go_to_demoqa_dynamic()
    assert py.contains('This text has random Id')


def test_element_with_dynamic_id_2(elements, py):
    elements.dynamic_properties.go_to_demoqa_dynamic()
    assert py.get('p').should().contain_text('This text has random Id')


def test_element_is_visible_after_5_seconds(elements, py):
    elements.dynamic_properties.go_to_demoqa_dynamic()
    assert py.get('#visibleAfter').should().be_visible()


def test_element_enabled_after_5_seconds(elements, py):
    elements.dynamic_properties.go_to_demoqa_dynamic()
    button = py.get('#enableAfter')
   # assert button.should().not_have_attr('disabled')
    assert py.get('#enableAfter').should().not_have_attr('disabled')
    assert py.wait().until(lambda _: button.is_enabled())


def test_element_changes_text_color_to_red(elements, py):
    elements.dynamic_properties.go_to_demoqa_dynamic()
    color_button = py.get('#colorChange')
    assert py.wait().until(lambda _: 'danger' in color_button.get_attribute('class'))



