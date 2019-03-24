# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv


phones = []

def load_phone_list():
    if os.access("myphones1.csv",os.F_OK):
        f = open("myphones1.csv")
        for row in csv.reader(f):
            phones.append(row)
        f.close()
        
def reorder_phones():
    global phones       # this insures that we use the one at the top
    load_phone_list()
    phones.sort()
    save_phone_list()
    
def save_phone_list():

    f = open("myphones.csv", 'w', newline='')
    for item in phones:
        csv.writer(f).writerow(item)
    f.close()
    
if __name__ == '__main__':
     reorder_phones()