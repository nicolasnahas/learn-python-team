"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_conditional_expression():
    """Conditional expressions (the "ternary" if).

    A conditional expression has the form `value_if_true if condition else value_if_false`.
    It lets us choose between two values on a single line instead of writing a full
    if ... else block.
    """

    number = 7

    if number % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'

    assert parity == 'odd'

    assert ('even' if number % 2 == 0 else 'odd') == 'odd'
    assert ('even' if 10 % 2 == 0 else 'odd') == 'even'

    labels = ['even' if n % 2 == 0 else 'odd' for n in range(4)]
    assert labels == ['even', 'odd', 'even', 'odd']


def test_if_with_truthiness_and_combined_conditions():
    """Truthy/falsy values and combining conditions with and, or, not.

    An if statement does not need a real boolean. Values such as 0, '' (empty string),
    [] (empty list), {} (empty dict) and None are treated as False ("falsy"); almost
    everything else is treated as True ("truthy"). Conditions can be combined with
    the keywords and, or and not.
    """

    for falsy_value in [0, '', [], {}, None]:
        entered = False
        if falsy_value:
            entered = True
        assert entered is False

    for truthy_value in [1, 'text', [0], {'key': 'value'}]:
        entered = False
        if truthy_value:
            entered = True
        assert entered is True

    age = 25
    has_ticket = True

    if age >= 18 and has_ticket:
        can_enter = True
    else:
        can_enter = False

    assert can_enter is True

    is_weekend = False
    is_holiday = True
    assert (is_weekend or is_holiday) is True

    shopping_list = []
    if not shopping_list:
        message = 'Nothing to buy'
    else:
        message = 'Go shopping'

    assert message == 'Nothing to buy'


def test_nested_if_letter_grade():
    """Nested if statements and elif chains.

    An elif chain checks conditions from top to bottom and runs only the first block whose
    condition is true. An if statement can also be placed inside another if block (nested)
    to make a more specific decision once the outer condition is known.
    """

    def letter_grade(score):
        if score < 0 or score > 100:
            return 'Invalid'

        if score >= 90:
            letter = 'A'
        elif score >= 80:
            letter = 'B'
        elif score >= 70:
            letter = 'C'
        elif score >= 60:
            letter = 'D'
        else:
            return 'F'

        last_digit = score % 10
        if letter == 'A':
            if score == 100 or last_digit >= 7:
                return 'A+'
            elif last_digit <= 2:
                return 'A-'
        else:
            if last_digit >= 7:
                return letter + '+'
            elif last_digit <= 2:
                return letter + '-'

        return letter

    assert letter_grade(100) == 'A+'
    assert letter_grade(97) == 'A+'
    assert letter_grade(95) == 'A'
    assert letter_grade(90) == 'A-'
    assert letter_grade(88) == 'B+'
    assert letter_grade(85) == 'B'
    assert letter_grade(81) == 'B-'
    assert letter_grade(74) == 'C'
    assert letter_grade(68) == 'D+'
    assert letter_grade(59) == 'F'
    assert letter_grade(0) == 'F'
    assert letter_grade(-5) == 'Invalid'
    assert letter_grade(101) == 'Invalid'
