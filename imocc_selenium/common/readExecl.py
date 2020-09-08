from typing import List

import xlrd
import xlwt
from xlutils.copy import copy

class WriteExecl():
    def __init__(self,filename):
        self.filename=filename
        self.workbook=xlwt.Workbook(encoding="utf-8")
        self.sheet=self.workbook.add_sheet("sheet1")

    def write_tuple_list(self,data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.sheet.write(i,j,label=data[i][j])
        self.workbook.save(self.filename)


class ReadExecl():
    def __init__(self,filename,index=None):
        if index==None:
            index=0
        self.filename=filename
        self.data=xlrd.open_workbook(filename,encoding_override="utf8")
        self.sheet=self.data.sheet_by_index(index)
        self.rows=self.sheet.nrows


    def get_data(self):
        result=[]
        if self.get_rows()!=None:
            for i in range(self.get_rows()):
                data=self.sheet.row_values(i)
                result.append(data)
            return result
        else:
            return None

    def get_rows(self):
        if self.sheet.nrows>1:
            return self.sheet.nrows
        else:
            return None

    def get_cell_value(self,row,column):
        return self.sheet.cell_value(row,column)

    def write_cell(self,row,column,value):
        read_value=self.data
        new_workbook=copy(read_value)
        new_workbook.get_sheet(0).write(row,column,value)
        new_workbook.save(self.filename)


if __name__=="__main__":
    # data=[["a3", "37623001@qq.com", "12345678", "12345678","13172661165","username_error","用户名"],
    # ["a376230095", "37623001qq.com", "12345678", "12345678","13172661165","email_error", "邮件地址不合法"],
    # ["a376230095", "37623001@qq.com", "12", "12","13172661165","password_error", "登录密码不能少于"]]
    # a=WriteExecl("../data/text.xls")
    # a.write_tuple_list(data)
    a=ReadExecl("../data/text.xls")
    print(a.get_cell_value(1,1))
    a.write_cell(10,10,10)