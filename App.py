#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
    接口信息更新
    Document:
        1 字符串格式化函数 str.format()
            ·使用'{}'占位符   print('I\'m {},{}'.format('Hongten','Welcome to my space!'))
            ·使用'{0}','{1}'占位符 print('{0},I\'m {1},my E-mail is {2}'.format('Hello','Hongten','hongtenzone@foxmail.com'))
            ·可以改变占位符的位置   print('{1},I\'m {0},my E-mail is {2}'.format('Hongten','Hello','hongtenzone@foxmail.com'))
            ·使用'{name}'的占位符  print('Hi,{name},{message}'.format(name = 'Tom',message = 'How old are you?'))
            ·混合使用'{0}','{name}'  print('{0},I\'m {1},{message}'.format('Hello','Hongten',message = 'This is a test message!'))

"""

import sys
import BaiduService,DbService



def main():
    dbService = DbService.DbService()
    baiduService = BaiduService.BaiduService()
    # 查找需要执行的数据
    # select  userId,siteAddr,city from Com_User_Info where UserType='07' and Latitude is null and Longitude is null
    qSql = "select  top 1 userId,siteAddr,city from Com_User_Info where UserType='07' and Latitude is null and Longitude is null"

    rows = dbService.query(qSql)
    i = 0
    for (userId,siteAddr,city) in rows:
        rs = baiduService.translate(str(siteAddr).encode('latin1').decode('gbk'),str(city).encode('latin1').decode('gbk'))
        lng = str(rows['lng'])
        lat = str(rows['lat'])
        confidence = str(rows['confidence'])
        uSql = "update  Com_User_Info set Longitude="+lng[0:15]+",Latitude="+lat[0:15]+",Remark="+confidence+" where userId="+userId
        dbService.update(uSql)

if __name__ == '__main__':
    main()



