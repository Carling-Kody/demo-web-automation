

def test_accordian_landing_page_default(widgets, py):
    widgets.accordian.go_to_demoqa_accordian()
    assert py.get('#section1Content').contains('popularised in the 1960s')


def test_one_section_open(widgets, py):
    widgets.accordian.go_to_demoqa_accordian()
    test = py.getx("//div[@class='card'][1]//").get_attribute('class')  # f"(//button[@title='Toggle'])[{index}]"
    test2 = py.getx("//div[@class='card'][2]").text()
    test3 = py.getx("//div[@class='card'][3]").text()
    # test4 = py.getx("//div[@id='section1Content']/div")
    print(test)
    print(test2)
    print(test3)