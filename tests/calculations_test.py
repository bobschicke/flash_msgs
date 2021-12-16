""" These are the tests for the Calculation History """
import pytest
from history.calculations import Calculations
from calc.addition import Addition


@pytest.fixture
def clear_hist():
    """ Clears the history in calc_history list """
    Calculations.clear_calc_history()


@pytest.fixture
def setup_calcs_fixture():
    """ Clears the history in calc_history list """
    addition = Addition((2, 3))
    Calculations.add_calculation_to_history1(addition)
    addition = Addition((4, 5))
    Calculations.add_calculation_to_history1(addition)

# pylint: disable=unused-argument, redefined-outer-name
def test_get_last_result(clear_hist, setup_calcs_fixture):
    """ Tests that the function returns the last result in calc_history """
    assert Calculations.get_last_result_in_history() == 9


def test_get_first_result(clear_hist, setup_calcs_fixture):
    """ Tests that the function returns the first result in calc_history """
    assert Calculations.get_first_result_in_history() == 5


def test_count_history(clear_hist, setup_calcs_fixture):
    """ Tests that the number of calculations in calc_history is correct """
    assert Calculations.count_history() == 2


def test_get_history(clear_hist, setup_calcs_fixture):
    """ The return value of get_calc_history() is a list of the calculation results from history"""
    # This tests that the returned list has the calculation history results
    # in order from oldest to newest
    # clear_hist()
    # get_calc_history
    assert Calculations.count_history() == 2
    hist_list =  Calculations.get_calc_result_history1()
    assert len(hist_list) == 2
    assert  hist_list[0] == 5
    assert hist_list[1] == 9


def test_clear_hist(clear_hist, setup_calcs_fixture):
    """ Tests that calc_history list is cleared """
    # clear_hist()
    assert Calculations.count_history() == 2
    assert Calculations.clear_calc_history() is True
    assert Calculations.count_history() == 0
