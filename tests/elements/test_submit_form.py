

def test_submit_form(py):
    py.visit('https://demoqa.com/text-box')
    py.get("#userName").type('Kody Carling')
    py.get("#userEmail").type('kodycarling19@gmail.com')
    py.get("#currentAddress").type('2055 E 160 S Spanish Fork, Utah 84660')
    py.get("#permanentAddress").type(py.fake.address())
    py.get("#submit").click()
    assert py.get('p[id="name"]').should().contain_text('Kody Carling')


# refactor
