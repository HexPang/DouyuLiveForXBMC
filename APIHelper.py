# -*- coding: utf-8 -*-
# 斗鱼接口
import urllib2
import json


class APIHelper:
    def __init__(self):
        self.baseUrl = "http://api.douyutv.com/api/client"
        self.client_sys = "android"

    def request(self, url, param=None):
        reqUrl = url
        if param != None:
            for k, v in enumerate(param):
                reqUrl = reqUrl + "&" + v + "=" + param[v]
        try:
            response = urllib2.urlopen(reqUrl, timeout=10).read()
            jsonObject = json.loads(response)
            data = jsonObject["data"]
            return data
        except Exception, e:
            print "Error:" + str(e)
        return None