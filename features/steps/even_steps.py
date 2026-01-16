from behave import given, when, then
# TODO: Importáld a number_checker modult a src mappából
from src.number_checker import check_number

# TODO: Implementáld a Given step-et
#@given('the number is 4')
#def step_given_number(context):
#    context.number = 4

#@given('the number is 5')
#def step_given_number(context):
#    context.number = 5

#@given('the number is 0')
#def step_given_number(context):
#    context.number = 0

@given('the number is "{number}"')
def step_given_number(context, number):
    context.number = int(number)

# TODO: Implementáld a When step-et
# Használd a check_number függvényt a src/number_checker.py fájlból!
@when("I ask whether it's even or odd")
def step_when_check_number(context):
    context.result = check_number(context.number)


# TODO: Implementáld a Then step-et
@then('I should be told "{expected_answer}"')
def step_when_I_ask_whether_its_even_or_odd(context, expected_answer):
    assert context.result == expected_answer
