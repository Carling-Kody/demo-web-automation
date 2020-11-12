
# Both of these tests should fail.

def test_range_value_equals_input_value(widgets, py):
    widgets.slider.go_to_demoqa_slider()
    slider = py.get("input.range-slider")
    slider_input = py.get("#sliderValue")
    py.execute_script('arguments[0].value="10";', slider.webelement)
    assert slider_input.should().have_value('10')


def test_range_value_slid_left(widgets, py):
    widgets.slider.go_to_demoqa_slider()
    slider = py.get("input.range-slider")
    slider_input = py.get("#sliderValue")
    py.execute_script('arguments[0].value="40";', slider_input.webelement)
    assert slider.should().have_value('40')


