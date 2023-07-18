import glob
import os
import pandas as pd
from datetime import datetime
import sys
import random
import calendar
import colorama
from colorama import Fore, Style



def convert_data(year, directory, directory_name, output_file_path):
    files = glob.glob(os.path.join(directory, f"{directory_name}_{year}_*.txt"))    
    try:
        with open(output_file_path, "w") as output_file:
            for file_path in files:
                with open(file_path, "r+") as input_file:
                    data_frame = pd.read_csv(file_path)
                    data_frame = data_frame.fillna(0)
                    df_string = data_frame.to_string(index=False, header=False)
                    output_file.write(df_string)
                    output_file.write("\n")
    except:
        print("Invalid Path !!")


# ------------------------------------------------------------------------------
# CONVERSION FOR GIVEN MONTH
# ------------------------------------------------------------------------------
def display_month(month, year, directory, directory_name):
    file = glob.glob(os.path.join(directory, f"{directory_name}_{year}_{month}.txt"))    
    try:
        file_name = file[0]
        with open(file_name, "r+") as input_file:
            data_frame = pd.read_csv(file_name)
            data_frame = data_frame.fillna(0)
            df_string = data_frame.to_string(index=False)
            # print(df_string)
            input_file.write(df_string)
    except:
        print("Invalid Path !!")


# ------------------------------------------------------------------------------
# finding average of highest temperature
# ------------------------------------------------------------------------------
def find_high_avg(month, year, directory, directory_name):
    file = glob.glob(os.path.join(directory, f"{directory_name}_{year}_{month}*.txt"))
    try:
        file_name = file[0]
        column_index = 1
        values = []
        with open(file_name, "r") as file:
            next(file)
            lines = file.readlines()
            for line in lines:
                columns = line.split()
                if column_index < len(columns):
                    value = columns[column_index]
                    float_num = float(value)
                    values.append(float_num)
        average = sum(values) / len(values)
        print("Highest Average : ", round(average, 1), "C")
    except:
        print("Invalid Path !!")

# ------------------------------------------------------------------------------
# finding avg of lowest temp
# ------------------------------------------------------------------------------
def find_lowest_avg(month, year, directory, directory_name):
    file = glob.glob(os.path.join(directory, f"{directory_name}_{year}_{month}*.txt"))
    try:
        file_name = file[0]
        column_index = 3
        values = []
        with open(file_name, "r") as file:
            next(file)
            lines = file.readlines()
            for line in lines:
                columns = line.split()
                if column_index < len(columns):
                    value = columns[column_index]
                    float_num = float(value)
                    values.append(float_num)
        average = sum(values) / len(values)
        print("Lowest Average : ", round(average, 1), "C")
    except:
        print("Invalid Path !!")

# ------------------------------------------------------------------------------
# finding avg of humidity
# ------------------------------------------------------------------------------
def find_avg_humid(month, year, directory, directory_name):
    file = glob.glob(os.path.join(directory, f"{directory_name}_{year}_{month}*.txt"))
    try:
        file_name = file[0]
        column_index = 7
        values = []
        with open(file_name, "r") as file:
            next(file)
            lines = file.readlines()
            for line in lines:
                columns = line.split()
                if column_index < len(columns):
                    value = columns[column_index]
                    float_num = float(value)
                    values.append(float_num)

        average = sum(values) / len(values)
        print("Average Humidity : ", round(average, 1), "%")
    except:
        print("Invalid Path !!")

# ------------------------------------------------------------------------------
# FIND MAX TEMP
# ------------------------------------------------------------------------------
def find_max():
    max_index = 0
    max_value = 0
    try:
        file_pattern = f"{directory_name}_output_file_{year}.txt"
        column_index = 1
        values = []
        with open(file_pattern, "r") as file:
            lines = file.readlines()
            for line in lines:
                columns = line.split()
                if column_index < len(columns):
                    value = columns[column_index]
                    float_num = float(value)
                    values.append(float_num)
        for i, num in enumerate(values):
            if num > max_value:
                max_value = num
                max_index = i
        return max_value, max_index
    except:
        print("Invalid !!")

# ------------------------------------------------------------------------------
# FIND MINIMUM TEMP
# ------------------------------------------------------------------------------
def find_min():
    min_index = 0
    min_value = float("inf")
    file_pattern = f"{directory_name}_output_file_{year}.txt"
    column_index = 3
    values = []
    try:
        with open(file_pattern, "r") as file:
            lines = file.readlines()
            for line in lines:
                columns = line.split()
                if column_index < len(columns):
                    value = columns[column_index]
                    float_num = float(value)
                    values.append(float_num)
        for i, num in enumerate(values):
            if num < min_value:
                min_value = num
                min_index = i

        return min_value, min_index
    except:
        print("Invalid Path !! ")

# ------------------------------------------------------------------------------
# FIND HUMIDITY
# ------------------------------------------------------------------------------
def find_humid():
    max_index = 0
    max_value = 0
    file_pattern = f"{directory_name}_output_file_{year}.txt"
    column_index = 7
    values = []
    try:
        with open(file_pattern, "r") as file:
            lines = file.readlines()
            for line in lines:
                columns = line.split()
                if column_index < len(columns):
                    value = columns[column_index]
                    float_num = float(value)
                    values.append(float_num)
        for i, num in enumerate(values):
            if num > max_value:
                max_value = num
                max_index = i
        return max_value, max_index
    except:
        print("Invalid Path !!")

# ------------------------------------------------------------------------------
# CONVERSION TO DATE FORMAT
# ------------------------------------------------------------------------------
def Dateformat(temp, i, j):
    try:
        file = open(f"{directory_name}_output_file_{year}.txt")
        content = file.readlines()
        line = content[i].split()
        date = str(line[0])
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        month_name = date_obj.strftime("%B")
        day = date_obj.day
        yr = date_obj.year
        if j == 1:
            print("Highest:", temp, "C on", month_name, day)
        if j == 2:
            print("Lowest:", temp, "C on", month_name, day)
        if j == 3:
            print("Humidity:", temp, "%", " on", month_name, day)
    except:
        print("Invalid Path !!")
# ---------------------------------------------------------------------------------------
# horizontal bar charts
# ---------------------------------------------------------------------------------------
def draw(month, i, year, directory, directory_name):
    try:
        file = glob.glob(os.path.join(directory, f"{directory_name}_{year}_{month}.txt"))
        file_name = file[0]
        max_temp_index = 1
        min_temp_index = 3
        max_number = []
        min_number = []
        days_list = []
        _, days = calendar.monthrange(year, i)
        with open(file_name, "r") as file:
            next(file)
            lines = file.readlines()
            for line in lines:
                columns = line.split()
                if max_temp_index < len(columns):
                    value = columns[max_temp_index]
                    max_number.append(float(value))
                if min_temp_index < len(columns):
                    value = columns[min_temp_index]
                    min_number.append(float(value))
            max_color = Fore.BLUE
            min_color = Fore.RED
            j = 1
            while days != 0:
                days_list.append(j)
                j = j + 1
                days = days - 1
            iteration = 0
            for i in days_list:
                plus_max = max_color + "+" * int(round(max_number[iteration]))
                print(i, plus_max, int(round(max_number[iteration])), "C")
                plus_min = min_color + "+" * int(round(min_number[iteration]))
                print(i, plus_min, int(round(min_number[iteration])), "C")
                iteration = iteration + 1
            iteration = 0
            for i in days_list:
                m = int(round(max_number[iteration]))
                n = int(round(min_number[iteration]))
                plus_ = max_color + "+" * m + min_color + "+" * n
                print(i, plus_, Fore.BLUE + str(m), "-", Fore.RED + str(n))
                iteration = iteration + 1
    except:
        print("Invalid Path !!")

try:
    flag = sys.argv[1]

    if flag == "-e":
        year = int(sys.argv[2])
        directory = sys.argv[3]
        directory_name = os.path.basename(os.path.normpath(directory))
        output_file_path = f"{directory_name}_output_file_{year}.txt"
        if (directory_name == "Murree_weather") and (year < 2004 or year > 2016):
            print("Invalid Input")
        elif (directory_name == "lahore_weather") and (year < 1996 or year > 2011):
            print("Invalid Input")
        elif (directory_name == "Dubai_weather") and (year < 2004 or year > 2016):
            print("Invalid Input")
        else:
            convert_data(year, directory, directory_name, output_file_path)
            max_temp, max_index = find_max()
            min_temp, min_index = find_min()
            max_humid, min_humid = find_humid()
            Dateformat(max_temp, max_index, 1)
            Dateformat(min_temp, min_index, 2)
            Dateformat(max_humid, min_humid, 3)
    elif flag == "-a":
        mh = int(sys.argv[3])
        yr = int(sys.argv[2])
        d = sys.argv[4]
        path_ = os.path.normpath(d)
        directory = os.path.dirname(path_)
        directory_name = os.path.basename(os.path.normpath(directory))
        if (directory_name == "Murree_weather") and (yr < 2004 or yr > 2016):
            print("Invalid Input")
        elif (directory_name == "lahore_weather") and (yr < 1996 or yr > 2011):
            print("Invalid Input")
        elif (directory_name == "Dubai_weather") and (yr < 2004 or yr > 2016):
            print("Invalid Input")
        else:
            if mh == 1:
                display_month("Jan", yr, directory, directory_name)
                find_high_avg("Jan", yr, directory, directory_name)
                find_lowest_avg("Jan", yr, directory, directory_name)
                find_avg_humid("Jan", yr, directory, directory_name)
            elif mh == 2:
                display_month("Feb", yr, directory, directory_name)
                find_high_avg("Feb", yr, directory, directory_name)
                find_lowest_avg("Feb", yr, directory, directory_name)
                find_avg_humid("Feb", yr, directory, directory_name)
            elif mh == 3:
                display_month("Mar", yr, directory, directory_name)
                find_high_avg("Mar", yr, directory, directory_name)
                find_lowest_avg("Mar", yr, directory, directory_name)
                find_avg_humid("Mar", yr, directory, directory_name)
            elif mh == 4:
                display_month("Apr", yr, directory, directory_name)
                find_high_avg("Apr", yr, directory, directory_name)
                find_lowest_avg("Apr", yr, directory, directory_name)
                find_avg_humid("Apr", yr, directory, directory_name)
            elif mh == 5:
                display_month("May", yr, directory, directory_name)
                find_high_avg("May", yr, directory, directory_name)
                find_lowest_avg("May", yr, directory, directory_name)
                find_avg_humid("May", yr, directory, directory_name)
            elif mh == 6:
                display_month("Jun", yr, directory, directory_name)
                find_high_avg("Jun", yr, directory, directory_name)
                find_lowest_avg("Jun", yr, directory, directory_name)
                find_avg_humid("Jun", yr, directory, directory_name)
            elif mh == 7:
                display_month("Jul", yr, directory, directory_name)
                find_high_avg("Jul", yr, directory, directory_name)
                find_lowest_avg("Jul", yr, directory, directory_name)
                find_avg_humid("Jul", yr, directory, directory_name)
            elif mh == 8:
                display_month("Aug", yr, directory, directory_name)
                find_high_avg("Aug", yr, directory, directory_name)
                find_lowest_avg("Aug", yr, directory, directory_name)
                find_avg_humid("Aug", yr, directory, directory_name)
            elif mh == 9:
                display_month("Sep", yr, directory, directory_name)
                find_high_avg("Sep", yr, directory, directory_name)
                find_lowest_avg("Sep", yr, directory, directory_name)
                find_avg_humid("Sep", yr, directory, directory_name)
            elif mh == 10:
                display_month("Oct", yr, directory, directory_name)
                find_high_avg("Oct", yr, directory, directory_name)
                find_lowest_avg("Oct", yr, directory, directory_name)
                find_avg_humid("Oct", yr, directory, directory_name)
            elif mh == 11:
                display_month("Nov", yr, directory, directory_name)
                find_high_avg("Nov", yr, directory, directory_name)
                find_lowest_avg("Nov", yr, directory, directory_name)
                find_avg_humid("Nov", yr, directory, directory_name)
            elif mh == 12:
                display_month("Dec", yr, directory, directory_name)
                find_high_avg("Dec", yr, directory, directory_name)
                find_lowest_avg("Dec", yr, directory, directory_name)
                find_avg_humid("Dec", yr, directory, directory_name)
            else:
                print("Invalid Input Month")
                
    elif flag == "-c":
        mh = int(sys.argv[3])
        yr = int(sys.argv[2])
        d = sys.argv[4]
        path_ = os.path.normpath(d)
        directory = os.path.dirname(path_)
        directory_name = os.path.basename(os.path.normpath(directory))
        if (directory_name == "Murree_weather") and (yr < 2004 or yr > 2016):
            print("Invalid Input")
        elif (directory_name == "lahore_weather") and (yr < 1996 or yr > 2011):
            print("Invalid Input")
        elif (directory_name == "Dubai_weather") and (yr < 2004 or yr > 2016):
            print("Invalid Input")
        else:
            if mh == 1:
                display_month("Jan", yr, directory, directory_name)
                draw("Jan", mh, yr, directory, directory_name)

            elif mh == 2:
                display_month("Feb", yr, directory, directory_name)
                draw("Feb", mh, yr, directory, directory_name)

            elif mh == 3:
                display_month("Mar", yr, directory, directory_name)
                draw("Mar", mh, yr, directory, directory_name)

            elif mh == 4:
                display_month("Apr", yr, directory, directory_name)
                draw("Apr", mh, yr, directory, directory_name)

            elif mh == 5:
                display_month("May", yr, directory, directory_name)
                draw("May", mh, yr, directory, directory_name)

            elif mh == 6:
                display_month("Jun", yr, directory, directory_name)
                draw("Jun", mh, yr, directory, directory_name)

            elif mh == 7:
                display_month("Jul", yr, directory, directory_name)
                draw("Jul", mh, yr, directory, directory_name)

            elif mh == 8:
                display_month("Aug", yr, directory, directory_name)
                draw("Aug", mh, yr, directory, directory_name)

            elif mh == 9:
                display_month("Sep", yr, directory, directory_name)
                draw("Sep", mh, yr, directory, directory_name)

            elif mh == 10:
                display_month("Oct", yr, directory, directory_name)
                draw("Oct", mh, yr, directory, directory_name)

            elif mh == 11:
                display_month("Nov", yr, directory, directory_name)
                draw("Nov", mh, yr, directory, directory_name)

            elif mh == 12:
                display_month("Dec", yr, directory, directory_name)
                draw("Dec", mh, yr, directory, directory_name)
            else:
                print("Invalid Input Month")
except:
    print("Invalid Input !!")
