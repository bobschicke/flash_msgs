"""This file is for testing the CSV file managment"""
import os
from csv_util.file_utils import Filehandler
from calculator.calculator import Calculator

def get_root_path():
    """This method gets the filename from path/filename"""
    absolute_path = os.path.abspath(__file__)
    end = absolute_path.find("tests")  # find current directory
    root_path = absolute_path[:end]
    print("root_path = " + root_path)
    return root_path


def test_read_csv():
    """This method tests reading in a CSV file"""
    root_path = get_root_path()
    nump_array = Filehandler.read_csv(root_path + "/tests/test.csv")
    assert len(nump_array) == 4  #4 rows of data

def test_do_calcs():
    """This method tests running the calculations"""
    # do_calcs (rec_num, row_array, func, calc_type, filename)
    assert Filehandler.do_calcs(1, [200,2,1,4,2], Calculator.add,
                                "Addition", "test") == 209
    assert Filehandler.do_calcs(1, [200,2,1,4,2], Calculator.subtract,
                                "Subtraction", "test") == 191
    assert Filehandler.do_calcs(1, [200,2,1,4,2], Calculator.multiply,
                                "Multiplication", "test") == 3200
    assert Filehandler.do_calcs(1, [200,2,1,4,2], Calculator.divide,
                                "Division", "test") == 12.5

def test_do_calcs_errors():
    """This method tests running the calculations"""
    # do_calcs (rec_num, row_array, func, calc_type, filename)
    assert Filehandler.do_calcs(1, [200,2,"x",4,2], Calculator.add, "Addition", "test") == "nan"
    assert Filehandler.do_calcs(1, [200,2,0,4,2], Calculator.divide, "Division", "test") == "DivBy0"
    assert len(Filehandler.error_log) == 2


def test_process_csv():
    """This method tests processing the CSV"""
    root_path = get_root_path()
    nump_arr = Filehandler.read_csv(root_path + "/tests/test.csv")
    Filehandler.process_csv(nump_arr, "test.csv")
    assert len(Filehandler.calc_log) == 22


def test_get_csv_hist():
    """This method tests processing the CSV"""
    temp_list = Filehandler.get_csv_result_history()
    assert len(temp_list) > 0
