# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  : lileilei
# @File    : case.py
from Interface.testHttp import TestApi
from common.get_cases import get_data
from common.log import LOG, logger
import os
from config.config_T import Config_Try_Num, TestPlanUrl
from common.panduan import assert_in

@logger('测试')
def testinterface(cases):
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust = []
    list_unknown = 0
    list_exption = 0
    error_num=0
    for i in range(len(cases)):
        while error_num<=Config_Try_Num+1:
            api = TestApi(cases[i]['method'], TestPlanUrl+cases[i]['url'], cases[i]['header'], cases[i]['para'])
            apijson = api.getJson()
            if apijson['code'] == 0:
                LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s' % (cases[i]['method'], cases[i]['url'], apijson, cases[i]['expect']))
                assert_re = assert_in(asserqiwang=cases[i]['expect'], fanhuijson=apijson)
                if assert_re['code'] == 0:
                    list_json.append(apijson['result'])
                    listrelust.append('pass')
                    list_pass += 1
                    error_num=0
                    break
                elif assert_re['code'] == 1:
                    if error_num <=Config_Try_Num:
                        error_num+=1
                        LOG.info('失败重试中')
                        continue
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num=0
                        list_fail += 1
                        listrelust.append('fail')
                        list_json.append(apijson['result'])
                        break
                elif assert_re['code'] == 2:
                    if error_num <Config_Try_Num:
                        error_num+=1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num=0
                        list_exption += 1
                        listrelust.append('exception')
                        list_json.append(assert_re['result'])
                        break
                else:
                    if error_num <Config_Try_Num:
                        error_num+=1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num=0
                        list_unknown += 1
                        listrelust.append('未知错误')
                        list_json.append('未知错误')
                        break
            else:
                if error_num <Config_Try_Num:
                    error_num+=1
                    LOG.info('失败重试中')
                else:
                    LOG.info('失败重试中次数用完，最后结果')
                    error_num=0
                    list_exption += 1
                    listrelust.append('exception')
                    list_json.append(apijson['result'])
                    break
    return listrelust, list_fail, list_pass, list_json, list_exption, list_unknown