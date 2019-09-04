# Import modules for features not supported by base python install
import urllib.request
import csv
import codecs
import datetime
'''
Create the downloadDATA function

Use urllib.request ( urllib2 really ) to instantiate the
csvstream variable

use csv.reader to read from the csvstream and put it in the variable
csv_data
turn it into a list with list()
return data
'''
def downloadDATA(url):
    print(url)
    csvstream = urllib.request.urlopen(url)
    csv_data = csv.reader(codecs.iterdecode(csvstream, 'utf-8'))
    data = list(csv_data)
    return data

url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
url_data = downloadDATA(url)
#print(url_data)
'''
Create the processData function that takes in the csv_data
from downloadDATA

Loop through the array and access the values
0 - ID
1 - name
2 - date
Validate the date using dateTime
'''

def processData(url_data):
    for data in url_data:
        print(data[2])
        # The csv files first line is a header file, we need to skip it
        if data[2] == 'birthday':
            continue
        try:
            datetime.datetime.strptime(data[2], '%d/%m/%Y')
        except ValueError:
            # Replace the print with the logging to a file
            print(ValueError("Incorrect data format, should be DD/MM/YYYYY"))

processData(url_data)
