# -*- coding: utf-8 -*-
# @Author  : leizi
import os,datetime,time
from testCase.case import testinterface
from common.py_Html import createHtml
from common.get_cases import get_data
from  common.Dingtalk import send_ding
'''执行测试的主要文件'''
def start_interface_html_http():
    starttime=datetime.datetime.now()
    day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir=os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(basdir, 'test_case_data')
    all_case = get_data(path)
    listrelust, list_fail, list_pass, list_json,list_exption,list_unknown = testinterface(all_case)
    filepath =os.path.join(basdir+'\\test_Report\\%s-result.html'%day)
    # if os.path.exists(filepath) is False:
    #     os.system(r'touch %s' % filepath)
    endtime=datetime.datetime.now()
    listid = []
    listname = []
    listurl = []
    listmethod = []
    listexpect = []
    listheader = []
    listdata = []
    for i in range(len(all_case)):
        listid.append(all_case[i]['id'])
        listname.append(all_case[i]['casename'])
        listurl.append(all_case[i]['url'])
        listmethod.append(all_case[i]['method'])
        listexpect.append(all_case[i]['expect'])
        listheader.append(all_case[i]['header'])
        listdata.append(all_case[i]['para'])
    createHtml(titles=u'http接口自动化测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid ,name=listname,url=listurl,meth=listmethod, header =listheader, data = listdata,
               yuqi=listexpect,json=list_json,relusts=listrelust,unknown=list_unknown,exceptions=list_exption)
    contec = u'http接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
    list_pass, list_fail, list_exption, list_unknown, filepath)
    # send_ding(content=contec)
if __name__ == '__main__':
    start_interface_html_http()