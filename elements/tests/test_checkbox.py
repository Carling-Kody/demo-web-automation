def test_check_commands(elements, py):
    elements.checkboxes.go_to_demoqa_checkbox()
    elements.checkboxes.expand_first_toggle()
    elements.checkboxes.expand_carrot_toggles(2)
    elements.checkboxes.check_checkbox(4)
    assert py.get(".text-success").should().contain_text("commands")
    assert "half-check" in elements.checkboxes.check_for_checked_status(1)
    assert "half-check" in elements.checkboxes.check_for_checked_status(2)


def test_check_for_saved_state_after_closing(elements, py):
    elements.checkboxes.go_to_demoqa_checkbox()
    elements.checkboxes.expand_all()
    elements.checkboxes.check_checkbox(4)
    elements.checkboxes.check_checkbox(15)
    elements.checkboxes.close_all()
    elements.checkboxes.expand_first_toggle()
    assert "half-check" in elements.checkboxes.check_for_checked_status(1)
    assert "half-check" in elements.checkboxes.check_for_checked_status(2)
    assert "uncheck" in elements.checkboxes.check_for_checked_status(3)
    assert "icon-check" in elements.checkboxes.check_for_checked_status(4)
    assert "icon-check" in elements.checkboxes.check_for_checked_status(15)
    assert "icon-check" in elements.checkboxes.check_for_checked_status(16)
    assert "icon-check" in elements.checkboxes.check_for_checked_status(17)


