

def test_submit_form(py):
    py.visit('https://demoqa.com/text-box')
    py.get("#userName").type('Kody Carling')
    py.get("#userEmail").type('kodycarling19@gmail.com')
    py.get("#currentAddress").type('2055 E 160 S Spanish Fork, Utah 84660')
    py.get("#permanentAddress").type(py.fake.address())
    py.get("#submit").click()
    assert py.get('p[id="name"]').should().contain_text('Kody Carling')


# refactor

def test_user1(elements, py):
    elements.text_box.go_to_demoqa()
    elements.text_box.type_user_name('kody1')
    elements.text_box.type_user_email('kody1@foo.com')
    elements.text_box.get_current_address()
    elements.text_box.get_permanent_address()
    elements.text_box.submit_form()
    assert py.get('p[id="name"]').should().contain_text('kody1')


def test_user2(elements, py):
    elements.text_box.go_to_demoqa()
    elements.text_box.type_user_name('kody3')
    elements.text_box.type_user_email('kody1@foo.com')
    elements.text_box.get_current_address()
    elements.text_box.get_permanent_address()
    elements.text_box.submit_form()
    assert py.get('p[id="name"]').should().contain_text('kody3')
