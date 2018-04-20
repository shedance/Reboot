import pymysql
import requests
import re
from bs4 import BeautifulSoup

if __name__ == "__main__":
    #Mysql数据库连接：host + port + user + passwd+ db数据库名+charset编码格式

    conn = pymysql.connect(host='127.0.0.1', port = 3306, user = 'root',passwd = '*******',db = 'financialdata',charset = 'UTF8')
    #使用cursor（）方法获取操作游标
    cursor = conn.cursor()

    #数据库第一张表使用字典存储字段
    cwzb_dict = {
        'EPS': '基本每股收益',
        'EPS_DILUTED': '摊薄每股收益',
        'GROSS_MARGIN': '毛利率',
        'ROLOANS': '贷款回报率',
        'ROTA': '总资产收益率',
        'ROEQUITY': '净资产收益率',
        'CURRENT_RATIO': '流动比率',
        'QUICK_RATIO': '速动比率',
        'CAPITAL_ADEQUACY': '资本充足率',
        'TOTAL_ASSET2TURNOVER': '资产周转率',
        'LOANS_DEPOSITS': '存贷比',
        'INVENTORY_TURNOVER': '存货周转率',
        'GENERAL_ADMIN_RATIO': '管理费用比率',
        'FINCOSTS_GROSSPROFIT': '财务费用比率',
        'TURNOVER_CASH': '销售现金比率',
        'YEAREND_DATE': '报表日期'
    }

    # 利润表
    lrb_dict = {'TURNOVER': '总营收',
                'OPER_PROFIT': '经营利润',
                'PBT': '除税前利润',
                'NET_PROF': '净利润',
                'EPS': '每股基本盈利',
                'DPS': '每股派息',
                'INCOME_INTEREST': '利息收益',
                'INCOME_NETTRADING': '交易收益',
                'INCOME_NETFEE': '费用收益',
                'YEAREND_DATE': '报表日期'}

    # 资产负债表
    fzb_dict = {
        'FIX_ASS': '固定资产',
        'CURR_ASS': '流动资产',
        'CURR_LIAB': '流动负债',
        'INVENTORY': '存款',
        'CASH': '现金及银行存结',
        'OTHER_ASS': '其他资产',
        'TOTAL_ASS': '总资产',
        'TOTAL_LIAB': '总负债',
        'EQUITY': '股东权益',
        'CASH_SHORTTERMFUND': '库存现金及短期资金',
        'DEPOSITS_FROM_CUSTOMER': '客户存款',
        'FINANCIALASSET_SALE': '可供出售之证券',
        'LOAN_TO_BANK': '银行同业存款及贷款',
        'DERIVATIVES_LIABILITIES': '金融负债',
        'DERIVATIVES_ASSET': '金融资产',
        'YEAREND_DATE': '报表日期'}

    # 现金流表
    llb_dict = {
        'CF_NCF_OPERACT': '经营活动产生的现金流',
        'CF_INT_REC': '已收利息',
        'CF_INT_PAID': '已付利息',
        'CF_DIV_REC': '已收股息',
        'CF_DIV_PAID': '已派股息',
        'CF_INV': '投资活动产生现金流',
        'CF_FIN_ACT': '融资活动产生现金流',
        'CF_BEG': '期初现金及现金等价物',
        'CF_CHANGE_CSH': '现金及现金等价物净增加额',
        'CF_END': '期末现金及现金等价物',
        'CF_EXCH': '汇率变动影响',
        'YEAREND_DATE': '报表日期'}

    # 总表
    table_dict = {'cwzb': cwzb_dict, 'lrb': lrb_dict, 'fzb': fzb_dict, 'llb': llb_dict}
    #表格
    #table_dict = {'cwzb':cwzb_dict}

    #访问请求头
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        #'Content-Type': 'application/x-www-form-urlencoded',
        #'Connection':'keep-alive',
        #'Host': 'quotes.money.163.com',
        #'Referer': 'http://quotes.money.163.com/hkstock/cwsj_00700.html',
        #'Cookie': '_ntes_nnid=0c8d3d330b0e8a567acd22b29790d8a6,1523410622668; _ntes_nuid=0c8d3d330b0e8a567acd22b29790d8a6; __utma=187553192.1045869988.1523410623.1523410623.1523410623.1; __utmz=187553192.1523410623.1.1.utmcsr=open.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __oc_uuid=d5fc0650-3d28-11e8-80e8-81370d4dcf69; mail_psc_fingerprint=f21c604fbc674b3d3347acd9a8b42106; P_INFO=herdance@163.com|1523497426|0|other|11&16|zhj&1520388439&mailuni#sic&510100#10#0#0|&0||herdance@163.com; vjuids=-c15bb9890.162dc8e0f99.0.e536e5217d918; vjlast=1524118720.1524118720.30; ne_analysis_trace_id=1524119440967; Province=028; City=028; _ntes_stock_recent_=1300700; _ntes_stock_recent_=1300700; _ntes_stock_recent_=1300700; NNSSPID=93189f7be1e946b3bf3632abf82b1ead; usertrack=ezq0pVrYPo+nnsnwBPb0Ag==; _ntes_hkstock_recent_=00700; _ntes_hkstock_recent_=00700; s_n_f_l_n3=d8b71737821d3e011524140341213; vinfo_n_f_l_n3=d8b71737821d3e01.1.1.1524118720432.1524121254831.1524147172842'
    }

    #url爬取的地址
    url = 'http://quotes.money.163.com/hkstock/cwsj_00700.html'
    req = requests.get(url = url, headers = headers)
    req.encoding = 'utf-8'
    html = req.text
    html2 = req.content
    bs2 = BeautifulSoup(html,'lxml')
    bs = BeautifulSoup(html,'lxml')
    #股票名称，股票代获取
    #print(bs.prettify())
    name = bs.find_all('span',class_='name')[0].string
    code = bs.find_all('span',class_='code')[0].string
    code2 = bs.find_all('span', class_='code')[0].string

    print (type(code2))
    #将BeautifulSoup得到的NavigableString类型转为Str类型或者Int,根据情况而定
    nStr = ""
    nStr =nStr.join(code2)
    pNumr = str(nStr) #此处得到的pNumr的文本string类型 （00700）
    #print (type(pNumr))
    #print("转换后的文本：", pNumr)
    #怎么去掉括号？？？？？？
    code3 = re.sub('[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+','',pNumr)

    print('去掉括号了吗？：',code3)
    #打印股票信息
    print(name + ':' + code)
    print('')
    #存储各个表名的列表数据
    table_name_list = []
    table_date_list =[]
    each_date_list =[]
    url_list = []
    #表名和表时间
    table_name = bs.find_all('div',class_='titlebar3')
    for each_table_name in table_name:
        #表名
        table_name_list.append(each_table_name.span.string)
        #表时间
        for each_table_date in each_table_name.div.find_all('select', id = re.compile('.+1$')):
            url_list.append(re.findall('(\w+)1', each_table_date.get('id'))[0])
            for each_date in each_table_date.find_all('option'):
                each_date_list.append(each_date.string)
            table_date_list.append(each_date_list)
            each_date_list = []

    #插入信息
    #print("table_name_list是：",table_name_list)
    #print(len(table_name_list))
    for i in range(len(table_name_list)):
        print('表名',table_name_list[i])
        print(' ')

        #获取数据地址
        url2 = 'http://quotes.money.163.com/hk/service/cwsj_service.php?symbol={}&start={}&end={}&type={}&unit=yuan'.format(code3,table_date_list[i][-1],table_date_list[i][0],url_list[i])
        req_table = requests.get(url=url2, headers=headers)
        #print(req_table.json())
        print (url2)
        #print('url_list这是什么：',url_list)
        value_dict = {}
        for each_data in req_table.json():
            value_dict['股票名'] = name
            value_dict['股票代码'] = code3
            for key, value in each_data.items():
                #print(each_data)
                #print("key是什么：",key)
                #print(table_dict[url_list[i]])
                if key in table_dict[url_list[i]]:
                    value_dict[table_dict[url_list[i]][key]]=value
            #print("value_dict是什么",value_dict)
            #print('股票名',value_dict['股票名'])
            #print("股票名类型：", type(value_dict['股票名']))
            #将股票名类型转为string
            nStr1= ""
            nStr1 = nStr1.join(value_dict['股票名'])
            pNumr1 = str(nStr1)
            #print('股票名转化后：',pNumr1)
            #将报表日期转化为string类型
            nStr2 = ""
            nStr2 = nStr2.join(value_dict['报表日期'])
            pNumr2 = str(nStr2)
            #print('报表日期',value_dict['报表日期'])
            sql1 = "INSERT INTO %s (`股票名`,`股票代码`,`报表日期`) VALUES ('%s','%s','%s')"%(url_list[i],pNumr1,value_dict['股票代码'],pNumr2)
            #print(sql1)
            try:
                cursor.execute(sql1)
                #执行sql语句
                conn.commit()

            except:
                #发生错误时回滚
                conn.rollback()

            for key, value in value_dict.items():
                if key not in ['股票名','股票代码','报表日期']:
                    #sql语句注意` `和''的使用差别
                    sql2 = "UPDATE %s SET `%s`='%s' WHERE `股票名`='%s' AND `报表日期`='%s'"%(url_list[i],key,value,pNumr1,pNumr2)
                    print(sql2)
                    try:
                        cursor.execute(sql2)
                        #执行sql语句
                        conn.commit()
                    except:
                        #发生错误时回滚
                        conn.rollback()
                value_dict ={}
                #print(value_dict)

    #关闭数据库连接
    cursor.close()
    conn.close()



