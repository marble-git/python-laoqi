#coding:utf-8

'''
    filename:data2sqliteDB.py 
        chap:9
    subject:convert data to sqliteDB from excelfile
    conditions:modules: xlrd,sqlite3
    solution:
'''

import sqlite3
import xlrd


class Excel2SQLiteDB():
    '''convert every sheet in excelfile to tables in sqliteDB
    sheet name -> table name
    first row -> fields
    rows -> records
    '''
    def __init__(self,excelfile,sqliteDB = 'scores.SQLiteDB'):
        '''获取excel文件名和SQLite数据库名'''
        self.excelfile = excelfile
        self.sqliteDB = sqliteDB
        self.create_tables()



    def create_tables(self):
        '''在数据库中将该excel文件中包含的非空sheet
        转换为数据库table,
        并将sheet中的没行数据存入相应表的记录中'''


        #[创建/连接]数据库，
        #创建连接和游标对象
        self.conn = sqlite3.connect(self.sqliteDB)
        self.cur = self.conn.cursor()

        wb = xlrd.open_workbook(self.excelfile)
        ws_names = wb.sheet_names()     #获取sheet名称，作为数据库表名
        for ws_name in ws_names:
            ws = wb.sheet_by_name(ws_name)  #通过表名获取相应的sheet对象
            if ws.ncols == 0:
                continue    #过滤空sheet
            table_name = ws_name
            #将sheet中的第1行内容作为新建table中的fields
            #xlrd模块中，数据行和列从0索引
            fields = ws.row_values(0)  
            #默认所有单元格转储到数据库时全部保存为[text/纯文本格式]
            #将来可以增添按单元格数据类型的不同，采取不同的转储保存格式
            create_table = '''create table if not exists ''' + table_name + ' ' + str(tuple(field+' text' for field in fields)).replace(r"'",'')
            print(repr(create_table))
            self.cur.execute(create_table)
            #将[1,ws.nrows-1]行的数据转储到数据库table中
            for rowx in range(1,ws.nrows):
                insert_row = '''insert into ''' + table_name + ' values ' + str(tuple(ws.row_values(rowx)))
                self.cur.execute(insert_row)
        #提交更改并关闭游标，连接对象
        self.conn.commit()
        self.cur.close()
        self.conn.close()

            







if __name__ == '__main__':
    excelfile = input('Enter excelfile needed to be convert : ')
    Excel2SQLiteDB(excelfile)

