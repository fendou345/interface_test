# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

import xlrd
import os
from common.log import LOG, logger

@logger('解析测试用例文件')
#获取Excel里面的用例
def get_data(filepath):
    try:
        all_case = []
        filenames = os.listdir(filepath)
        for filename in filenames:
            excelpath = os.path.join(filepath, filename)
            data = xlrd.open_workbook(excelpath)
            sheets = data.sheet_names()
            for i in range(len(sheets)):
                sheet = sheets[i]
                table = data.sheet_by_name(sheet)
                nrows = table.nrows
                for j in range(1, nrows):
                    all_case.append({"id":table.cell_value(j, 0), "casename":table.cell_value(j, 1), "method":table.cell_value(j, 2),
                                     "url":table.cell_value(j, 3), "header":table.cell_value(j, 4), "para":table.cell_value(j, 5),
                                     "expect":table.cell_value(j, 6)})
        return all_case
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s' % e)
        return
# path = os.path.join(os.path.dirname(os.getcwd()), 'test_case_data')
# print(path)
# all_case = get_data(path)
# print(all_case)
# listid = []
# for i in range(len(all_case)):
#     listid.append(all_case[i]['id'])
#     # for key, value in all_case[i].items():
#     #     print(value)
# print(listid)