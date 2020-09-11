
def add(x, y):
    return x + y


def is_even(number):
    return number % 2 == 0


def test_adding_two_even_numbers_returns_even_number():
    output = add(2, 2)
    assert output == 4 and is_even(output)

def