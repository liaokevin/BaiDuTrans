#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    百度地图接口的封装
    百度地图Geocoding API服务地址：http://api.map.baidu.com/geocoder/v2/
    说明：
        域名：api.map.baidu.com
        服务名：geocoder
        服务版本号：较之前版本，v2版本新增参数。
"""
import sys,configparser
import urllib.request
import urllib.parse
import json

class BaiduService:
    api = ''
    ak = ''
    proxy = False
    ip =''
    port =''
    def __init__(self):
        """
        初始化
        :return:
        """
        cf = configparser.ConfigParser()    # 读取配置文件
        cf.read("config/config.conf")
        self.api = cf.get("baidu","api")
        self.ak = cf.get("baidu","ak")
        self.proxy = cf.get("http","proxy")
        self.ip = cf.get("http","ip")
        self.port = cf.get("http","port")

    def translate(self,location,city):
        """
        获取地址
        :param location: 详细地址
        :param city:城市
        :return:
        """
        rs= {'code':1,'lng': 0.0,'lat': 0.0,'confidence':0}
        location_cn = urllib.parse.quote(location,'UTF-8')  # 中文装换
        city_cn = urllib.parse.quote(city,'UTF-8')
        url = self.api+'?address='+location_cn+'&city='+city_cn+'&output=json&ak='+self.ak
        if True == self.proxy:
             try:
                proxy_handler = urllib.request.ProxyHandler({'http':self.ip+':'+self.port })  # 代理使用
                opener = urllib.request.build_opener(urllib.request.HTTPHandler,proxy_handler)
                rep = opener.open(url)
                if(rep.status==200):
                    data =  rep.read()  # 读取字节
                    strdata = str(data,'utf-8')  #  将字节转化成字符，形式 {"status":0,"result":{"location":{"lng":121.5614566934,"lat":31.299752270557},"precise":1,"confidence":70,"level":"\u5730\u4ea7\u5c0f\u533a"}}
                    print('获得的响应字符串为:'+strdata)
                    json_dict = json.loads(strdata) # 使用json模板将其转换成json字典，便可以使用get()方法来操作
                    if(json_dict.get('status')== 0):
                        rs['code']  = 0
                        rs['lng'] = json_dict.get('result').get('location').get('lng')
                        rs['lat'] = json_dict.get('result').get('location').get('lat')
                        rs['confidence'] = json_dict.get('result').get('confidence')

             except Exception as e:
                print(e)
             return rs
        else:
            try:
                rep = urllib.request.urlopen(url)
                if(rep.status==200):
                    data =  rep.read()  # 读取字节
                    strdata = str(data,'utf-8')  #  将字节转化成字符，形式 {"status":0,"result":{"location":{"lng":121.5614566934,"lat":31.299752270557},"precise":1,"confidence":70,"level":"\u5730\u4ea7\u5c0f\u533a"}}
                    print('获得的响应字符串为:'+strdata)
                    json_dict = json.loads(strdata) # 使用json模板将其转换成json字典，便可以使用get()方法来操作
                    if(json_dict.get('status')== 0):
                        rs['code']  = 0
                        rs['lng'] = json_dict.get('result').get('location').get('lng')
                        rs['lat'] = json_dict.get('result').get('location').get('lat')
                        rs['confidence'] = json_dict.get('result').get('confidence')
            except Exception as e:
                print(e)
            return rs



def main():
    p = BaiduService()
    print(p.translate('上海市','上海'))


if __name__ == '__main__':
    main()