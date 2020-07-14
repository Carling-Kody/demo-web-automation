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
    elements.checkboxes.expand_all_button()
    elements.checkboxes.check_checkbox('commands')
    elements.checkboxes.check_checkbox('downloads')
    elements.checkboxes.collapse_all_button()
    elements.checkboxes.expand_all_button()
    assert "half-check" in elements.checkboxes.check_for_checked_status('home')
    assert "half-check" in elements.checkboxes.check_for_checked_status('desktop')
    assert "uncheck" in elements.checkboxes.check_for_checked_status('notes')
    assert "icon-check" in elements.checkboxes.check_for_checked_status('commands')
    assert "icon-check" in elements.checkboxes.check_for_checked_status('downloads')
    assert "icon-check" in elements.checkboxes.check_for_checked_status('word file.doc')
    assert "icon-check" in elements.checkboxes.check_for_checked_status('excel file.doc')
    assert elements.checkboxes.check_success_message('commands') == 'commands'
    assert elements.checkboxes.check_success_message('downloads') == 'downloads'
    assert elements.checkboxes.check_success_message('wordFile') == 'wordFile'
    assert elements.checkboxes.check_success_message('excelFile') == 'excelFile'
    assert 'commands' in elements.checkboxes.get_success_messages()
    assert 'downloads' in elements.checkboxes.get_success_messages()
    assert 'wordFile' in elements.checkboxes.get_success_messages()
    assert 'excelFile' in elements.checkboxes.get_success_messages()







