from typing import List

import xlrd
import xlwt

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
        file=xlrd.open_workbook(filename,encoding_override="utf8")
        self.sheet=file.sheet_by_index(index)
        self.rows=self.sheet.nrows


    def get_data(self):
        result=[]
        for i in range(self.rows):
            data=self.sheet.row_values(i)
            result.append(data)
        return result

if __name__=="__main__":
    # data=[["a3", "37623001@qq.com", "12345678", "12345678","13172661165","username_error","用户名"],
    # ["a376230095", "37623001qq.com", "12345678", "12345678","13172661165","email_error", "邮件地址不合法"],
    # ["a376230095", "37623001@qq.com", "12", "12","13172661165","password_error", "登录密码不能少于"]]
    # a=WriteExecl("../data/text.xls")
    # a.write_tuple_list(data)
    a=ReadExecl("../data/text.xls")
    print(a.get_data())