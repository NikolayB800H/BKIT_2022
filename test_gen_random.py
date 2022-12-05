import pytest
from pytest_bdd import scenario, given, when, then, parsers
from process_data_to_test.gen_random import gen_random

@scenario('gen_random.feature', 'Giving count, begin and end')
def test_gen_random():
    pass

@given(parsers.parse("{num_count:d} numbers to generate from {begin:d} to {end:d}"))
def given_to_gen_random(num_count, begin, end):
    pytest.num_count = num_count
    pytest.begin = begin
    pytest.end = end
    pytest.tmp = gen_random(num_count, begin, end)

@when("using gen_random generator")
def generate():
    pytest.tmp_list = [i for i in pytest.tmp]

@then("I should get these numbers")
def check():
    assert len(pytest.tmp_list) == pytest.num_count
    for i in pytest.tmp_list:
        assert pytest.begin <= i <= pytest.end
