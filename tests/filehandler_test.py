"""This file is for testing the CSV file managment"""
import os
from csv_util.file_utils import Filehandler


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
    assert len(nump_array) == 4  # 4 rows of data


def test_get_logfile_path():
    """This method tests reading in a CSV file"""
    temp_path = Filehandler.get_logfile_path()
    assert temp_path == Filehandler.get_root_path() + 'logs/calc_log.csv'


# ([[int(time.time()), value1, value2, operation]])
def test_write_and_read_list_to_csv():
    """complete test of csv functionality"""
    Filehandler.write_vals_to_csv([[10, 20, 30, "add"]])
    Filehandler.delete_history()
    Filehandler.write_vals_to_csv([[10, 20, 30, "add"]])
    temp_list = Filehandler.get_csv_result_history()
    assert len(temp_list) == 1  # 1 row of data
