

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


def test_filter_user_by_email(elements, py):
    # Arrange
    email = 'cierra@example.com'
    elements.web_page_table.go_to_web_table_page()

    # Act
    elements.web_page_table.search_for_user(email)
    rows = py.find("[role='rowgroup']")

    # Assert
    # Filtered_rows=list()
    # for row in rows:
    #   if email in row.text():
    #        filtered_rows.append(row)
    filtered_rows = elements.web_page_table.get_filtered_rows_by_email(rows, email)
    assert len(filtered_rows) == 1


def test_emails_in_table_are_unique(py, elements):
    elements.web_page_table.go_to_web_table_page()
    populated_emails = elements.web_page_table.get_populated_emails()
    unique_emails = set(populated_emails)
    assert len(unique_emails) == len(populated_emails)
