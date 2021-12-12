"""This is a class to handle CSV files"""
import time
import os

import numpy
import pandas as pd
import numpy as np
from os.path import exists as file_exists
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
        #print("root_path = " + root_path)
        return root_path

    @staticmethod
    def get_logfile_path():
        return Filehandler.get_root_path() + 'logs/calc_log.csv'

    @staticmethod
    def write_to_csv(numpy_array):
        """Method to Write a Numpy array to a CSV file"""
        # np.savetxt("calc_log.csv", numpy_array, delimiter=",")
        dataframe = pd.DataFrame(numpy_array, columns= ['Rec_Num', 'Unix Time',
                                                 'Filename', 'Operation', 'Result'])
        # noinspection PyTypeChecker
        dataframe.to_csv(Filehandler.get_root_path() + 'logs/calc_log.csv', index= False)

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
    def append_vals_to_csv(numpy_array):
        """Method to Write a Numpy array to a CSV file"""
        # np.savetxt("calc_log.csv", numpy_array, delimiter=",")
        dataframe = pd.DataFrame(numpy_array, columns= ['Unix Time', 'Operation', 'val1', 'val2'])
        # noinspection PyTypeChecker
        dataframe.to_csv(Filehandler.get_root_path() + 'logs/calc_log.csv', index= False, header=False)



    @staticmethod
    def create_calc_log(rec_num, utime, filename, operation, result):
        """This is a method to collect log info in a numpy array"""
        temp_array = np.array([rec_num, utime, filename, operation, result])
        if len(Filehandler.calc_log) == 0:
            Filehandler.calc_log = np.append(Filehandler.calc_log, temp_array)
        else:
            Filehandler.calc_log = np.vstack([Filehandler.calc_log, temp_array])

    @staticmethod
    def create_error_log(rec_num, utime, filename, operation, result):
        """This is a method to collect log info in a numpy array"""
        temp_array = np.array([rec_num, utime, filename, operation, result])
        if len(Filehandler.error_log) == 0:
            Filehandler.error_log = np.append(Filehandler.error_log, temp_array)
        else:
            Filehandler.error_log = np.vstack([Filehandler.error_log, temp_array])

    @staticmethod
    def do_calcs (rec_num, row_array, func, calc_type, filename):
        """This method gets passed the function and an array and calls the calc function"""
        result = func(row_array) # todo pass operation here ("Calculator." + operation)(row_array) see if this works
        if isinstance(result, str):
            print("error = " + result)
            Filehandler.create_error_log(rec_num, time.time(), filename, calc_type, result)
        Filehandler.create_calc_log(rec_num, time.time(), filename, calc_type, result)
        return result

    # @staticmethod
    # def do_calc_operation(tuples, operation):
    #     """This method gets passed the operation and an array and calls the calc function"""
    #     result = operation(tuples) # todo pass operation here ("Calculator." + operation)(row_array) see if this works
    #     if isinstance(result, str):
    #         print("error = " + result)
    #         Filehandler.create_error_log(rec_num, time.time(), filename, calc_type, result)
    #     Filehandler.create_calc_log(rec_num, time.time(), filename, calc_type, result)
    #     return result


    @staticmethod
    def process_csv(nump_arr, filename : str):
        """This method iterates through the array and calls the calc functions"""
        rows, columns = nump_arr.shape
        print("Rows = " + str(rows) + ", Columns = " + str(columns))
        for row in range(rows):
            Filehandler.do_calcs((row * 4)+0, nump_arr[row],
                                 Calculator.add, "Addition", filename)
            Filehandler.do_calcs((row * 4)+1, nump_arr[row],
                                 Calculator.subtract, "Subtraction", filename)
            Filehandler.do_calcs((row * 4)+2, nump_arr[row],
                                 Calculator.multiply, "Multiplication", filename)
            Filehandler.do_calcs((row * 4)+3, nump_arr[row],
                                 Calculator.divide, "Division", filename)
        #print("calc_log:")
        #print(Filehandler.calc_log)
        #print("Writing to CSV") todo add flash messages
        Filehandler.write_to_csv(Filehandler.calc_log)
        Filehandler.write_to_csv(Filehandler.error_log)
        print('done')

    @staticmethod
    def read_csv(filesrcpath: str):
        """This method reads a CSV file and returns a numpy array"""
        #print("***pandas_csv.py***")
        dataframe = pd.read_csv(filesrcpath)
        #print(dataframe.columns)
        # pylint: disable=no-member
        nump_arr = dataframe.values
        #print("***Numpy array:***")
        #print(nump_arr)
        return nump_arr

    @staticmethod
    def get_csv_result_history():
        """ This returns a list of calculation results from oldest to newest """
        global VAL1, VAL2, OPERATION
        temp_list = []
        nump_array = Filehandler.read_csv(Filehandler.get_logfile_path())
        nump_list = nump_array.tolist()
        for row in nump_list:
            temp_row = row
            result = getattr(Calculator, row[OPERATION])([row[VAL1], row[VAL2]])
            #temp_row = numpy.append(temp_row, result)
            temp_row.append(result)
            temp_list.append(temp_row)
            #temp_list = numpy.append(temp_list, temp_row)
        return temp_list
