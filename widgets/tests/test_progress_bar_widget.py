

def test_progress(widgets, py):
    widgets.progress_bar.go_to_demoqa_progress_bar()
    default = py.get('#progressBar').get_attribute('outerText')
    py.get('#startStopButton').click()
    py.wait(use_py=True).sleep(3)
    py.get('#startStopButton').click()
    progress = py.get('#progressBar').get_attribute('outerText')
    assert default != progress


def test_progress_bar_value_not_saved(widgets, py):
    widgets.progress_bar.go_to_demoqa_progress_bar()
    py.get('#startStopButton').click()
    py.wait(use_py=True).sleep(3)
    py.get('#startStopButton').click()
    py.webdriver.refresh()
    py.get('#startStopButton').should().be_visible()
    assert py.get('#progressBar').get_attribute('outerText') == '0%'



