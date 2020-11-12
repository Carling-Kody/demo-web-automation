

def test_color_change_on_hover(widgets, py):
    widgets.menu.go_to_demoqa_menu()
    py.getx("//a[contains(text(),'Main Item 1')]").hover()


def test_sub_items_present(widgets, py):
    widgets.menu.go_to_demoqa_menu()
    py.getx("//a[contains(text(),'Main Item 2')]").hover()