from behave import given, when, then
from calc import run

@given(u'Calculator app is run')
def step_impl(context):
    print(u'STEP: Given Calculator app is run')
    pass

@when(u'I input "{inp}" to calculator')
def step_impl(context, inp):
    print(u'STEP: When I input "{}" to calculator'.format(inp))
    context.result = run(inp)

@then(u'I get result "{out}"')
def step_impl(context, out):
    print(u'STEP: Then I get result "{}"'.format(out))
    assert context.result == int(out), 'Expected {}, got {}'.format(out, context.result)
