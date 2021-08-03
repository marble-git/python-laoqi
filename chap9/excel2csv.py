#coding:utf-8

'''
    filename:excel2csv.py 
        chap:9
    subject:read data from an excel file,then write it into a csv file.
    conditions:modules:openpyxl,csv
    solution:func excel2csv
'''

import csv
import xlrd


def excel2csv(excelfile,csvfile):
    '''convert excel into csv'''
    wb = xlrd.open_workbook(excelfile)
    ws = wb.sheet_by_index(0)
    rows = (ws.row_values(i) for i in range(ws.nrows))
    with open(csvfile,'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)







if __name__ == '__main__':
    filenames = input('Enter Excel and CSV filenames [split with spaces]: ')
    excelname,csvname = filenames.split()
    excel2csv(excelname,csvname)
    pass

