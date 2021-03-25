''' Python Assignment for splitting the file based on size - Submitted by - Shashi Prakash 
    input format -> python main.py input.csv 
    input.csv is majestic million csv file, which contains recods over a million for testing purpose'''

import sys
from fsplit.filesplit import Filesplit

fs = Filesplit()

#Callback function to print the split outputs in the terminal 
def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))

#file -> input file name
#split_size -> size of every splits in bytes
#output_dir -> target directory to store the splits.
fs.split(file=sys.argv[1], split_size=1000000, output_dir="/home/shashi/Assignmnet/Splits", callback=split_cb)

