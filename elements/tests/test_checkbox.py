def test_check_commands(elements, py):
    elements.checkboxes.go_to_demoqa_checkbox()
    elements.checkboxes.expand_home_toggle_first_time()
    elements.checkboxes.expand_toggles(2)
    elements.checkboxes.check_checkbox(4)
    assert py.get(".text-success").should().contain_text("commands")
    assert "half-check" in elements.checkboxes.check_for_half_checked_status(1)
    assert "half-check" in elements.checkboxes.check_for_half_checked_status(2)



