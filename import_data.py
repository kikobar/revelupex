# Import necessary packages
import glob
import csv
import shutil
import re
from insert_order import insert_order
from insert_hourly import insert_hourly

# Import Oder History
path = "./upload/Order_History*.csv"
for filename in glob.glob(path):
    with open(filename) as file_obj:
        # Skips the heading 
        # Using next() method 
        heading = next(file_obj)
        
        # Create reader object by passing the file 
        # object to reader method 
        reader_obj = csv.reader(file_obj)
        
        # Iterate over each row in the csv file 
        # using reader object 
        for row in reader_obj:
	        print(row)
	        insert_order (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        shutil.move(filename, "history/")
        
# Import Hourly Sales
path = "./upload/Hourly_Sales*.csv"
for filename in glob.glob(path):
    print(filename)
    date = re.search(r'[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]', filename)
    print(date[0])
    with open(filename) as file_obj:
        heading = next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            if row[0] != 'Totals':
                print(row)
                insert_hourly (date[0], row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        shutil.move(filename, "history/")

