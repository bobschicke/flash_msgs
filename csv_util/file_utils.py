"""This is a class to handle CSV files"""
import os
from os.path import exists as file_exists
import pandas as pd
import numpy as np
from calculator.calculator import Calculator

UTIME = 0
VAL1 = 1
VAL2 = 2
OPERATION = 3
RESULT = 4


class Filehandler:
    """This is the Filehandler Class"""

    calc_log = np.array([])
    error_log = np.array([])

    @staticmethod
    def get_root_path():
        """This method gets the filename from path/filename"""
        absolute_path = os.path.abspath(__file__)
        end = absolute_path.find("csv_util")  # find current directory
        root_path = absolute_path[:end]
        # print("root_path = " + root_path)
        return root_path

    @staticmethod
    def get_logfile_path():
        """get logfile path method"""
        return Filehandler.get_root_path() + 'logs/calc_log.csv'

    @staticmethod
    def write_vals_to_csv(numpy_array):
        """Method to Write a Numpy array to a CSV file"""
        # noinspection PyTypeChecker
        # Get log filepath
        filepath = Filehandler.get_root_path() + 'logs/calc_log.csv'
        # Create Dataframe
        dataframe = pd.DataFrame(numpy_array, columns=['Unix Time', 'val1', 'val2', 'Operation'])
        # If file exists then append
        if file_exists(filepath):
            dataframe.to_csv(filepath, mode='a', index=False, header=False)
        # Else create the file
        else:
            dataframe.to_csv(filepath, index= False)

    @staticmethod
    def read_csv(filesrcpath: str):
        """This method reads a CSV file and returns a numpy array"""
        # print("***pandas_csv.py***")
        dataframe = pd.read_csv(filesrcpath)
        # print(dataframe.columns)
        # pylint: disable=no-member
        nump_arr = dataframe.values
        # print("***Numpy array:***")
        # print(nump_arr)
        return nump_arr

    @staticmethod
    def get_csv_result_history():
        """ This returns a list of calculation results from oldest to newest """
        global VAL1, VAL2, OPERATION
        temp_list1 = []
        nump_array = Filehandler.read_csv(Filehandler.get_logfile_path())
        nump_list = nump_array.tolist()
        for row in nump_list:
            temp_row1 = row
            result = getattr(Calculator, row[OPERATION])([row[VAL1], row[VAL2]])
            # temp_row = numpy.append(temp_row, result)
            temp_row1.append(result)
            temp_list1.append(temp_row1)
            # temp_list = numpy.append(temp_list, temp_row)
        return temp_list1

    @staticmethod
    def delete_history():
        """delete history method"""
        os.remove(Filehandler.get_logfile_path())
