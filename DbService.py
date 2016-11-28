#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    数据库连接服务
"""
import sys,configparser
import pymssql

class DbService:
    dbhost = ''
    dbuser = ''
    dbpasswd = ''
    dbdatabase = ''
    gconn=None

    def __init__(self):
        """
        初始化
        :return:
        """
        cf = configparser.ConfigParser()    # 读取配置文件
        cf.read("config/config.conf")
        self.dbhost = cf.get("database","dbhost")
        self.dbuser = cf.get("database","dbuser")
        self.dbpasswd = cf.get("database","dbpasswd")
        self.dbdatabase = cf.get("database","dbdatabase")

    def __openconn(self):
        """
        打开数据库连接
        :return:
        """
        self.gconn =  pymssql.connect(host=self.dbhost,user=self.dbuser,password=self.dbpasswd,database=self.dbdatabase,charset='UTF-8')

    def __closeconn(self):
        """
        关闭连接
        :return:
        """
        if None == self.gconn:
            print("")
        else:
            self.gconn.close()

    def query(self,sql):
        """
        查询语句
        :return:
        """
        try:
            self.__openconn();
            cursor = self.gconn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            self.gconn.commit()
            return rows
        except Exception as e:
          print(e)
        finally:
            self.__closeconn();

    def update(self,sql):
        """
        更新语句
        :param sql:
        :return:
        """
        try:
            self.__openconn();
            cursor = self.gconn.cursor()
            cursor.execute(sql)
            self.gconn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.__closeconn();



if __name__ == '__main__':
   p = DbService()
   print(p.query("select top 1 * from Com_User_Info"))
