import pymysql
import xlwt
from ShowProcess import ShowProcess
import time

def dbconnect(passwd):
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd=passwd,db='financialdata',charset='utf8')
    cursor =conn.cursor() #定义一个游标
    return cursor

if __name__=="__main__":
    passwd = input ("输入密码:")
    cursor= dbconnect(passwd)
    #cursor.execute("select `股票名`,`毛利率`,`报表日期` from cwzb")
    cursor.execute("select * from cwzb")
    #result = cursor.fetchall()
    #print(cursor.description)
    #print("============================================")
    #print(cursor.fetchone())
    #newdict = dict(zip([x[0] for x in cursor.description],[x for x in cursor.fetchone()]))  #将数据转化为字典
    #print('=============\n',newdict)
    #print(type(cursor.description))
    #print (result)
    #新建xls文件
    name=input("输入导入的excel档名称：")
    filename = name+'.xls'
    file_path = "F:\\MerciGo\Reports\\%s"%filename
    file= open(file_path,'w')
    wbk =xlwt.Workbook() #实例化一个Excel
    sheet1 = wbk.add_sheet('财务指标',cell_overwrite_ok=True) #创建sheet
    #fileds = ['股票名','毛利率','报表日期']#定义结果集的各字段
    fileds = cursor.description
    #print("fileds===========\n",fileds)
    result = cursor.fetchall()
    #print("==========\n",result)
    print(len(result))
    #写入字段到sheet中数据库中的字段写入到excel表的第一行中
    for i in range(0,len(fileds)):
        sheet1.write(0,i,fileds[i][0])

    # 写入sql查询到数据从excel的第二行开始进行写入
    max_steps = len(result)
    process_bar =ShowProcess(max_steps)
    for row in range(1, len(result) + 1):
        for col in range(0,len(fileds)):
            sheet1.write(row,col,result[row-1][col])
        process_bar.show_process()
        time.sleep(0.01)
    # 数据写入完成后保存excel
    wbk.save(file_path)
    process_bar.close("完成")
    file.close()
    print("完成数据导出至'%s'"%file_path)


