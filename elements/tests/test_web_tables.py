
def test_add_new_record_blank(elements, py):
    elements.web_page_table.go_to_web_table_page()
    elements.web_page_table.click_add_new_record_button()
    test_name = elements.web_page_table.type_first_name()
    elements.web_page_table.type_last_name()
    elements.web_page_table.type_email()
    elements.web_page_table.type_age()
    elements.web_page_table.type_salary()
    elements.web_page_table.type_department()
    elements.web_page_table.click_submit_new_record_button()

    assert py.get(".rt-tbody").contains(test_name)


def test_add_new_record_values(elements, py):
    elements.web_page_table.go_to_web_table_page()
    elements.web_page_table.click_add_new_record_button()
    elements.web_page_table.type_first_name("Kody")
    elements.web_page_table.type_last_name("Carling")
    elements.web_page_table.type_email("Kodycarling@workfront.com")
    elements.web_page_table.type_age("38")
    elements.web_page_table.type_salary("110000")
    elements.web_page_table.type_department("Product")
    elements.web_page_table.click_submit_new_record_button()

    assert py.get(".rt-tbody").contains("Kody")


def test_add_new_record_values(elements, py):
    elements.web_page_table.go_to_web_table_page()
    elements.web_page_table.add_new_record(first_name="Cody", last_name="Karling", email="kodycarling19@gmail.com",
                                           age="40", salary="120000", department="QA")
    assert py.get(".rt-tbody").contains("Cody")


def test_add_new_record_blank(elements, py):
    elements.web_page_table.go_to_web_table_page()
    check_name = elements.web_page_table.add_new_record()

    assert py.get(".rt-tbody").contains(check_name)

