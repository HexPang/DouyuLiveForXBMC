# -*- coding: utf-8 -*-
# 斗鱼接口
import urllib2
import json
from urllib import urlencode

class APIHelper:
    def __init__(self):
        self.baseUrl = ""

    def getUrl(self, action=""):
        if action == "":
            url = self.baseUrl
        else:
            if action.startswith("http"):
                url = action
            else:
                url = self.baseUrl + action
        return url

    def request(self, action, param=None):
        url = self.getUrl(action)
        if param is not None:
            url += "?" + urlencode(param)
        req = urllib2.Request(url)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(url).read()
        jsonobject = json.loads(response)
        return jsonobject

    def post(self, action, param):
        url = url = self.getUrl(action)
        req = urllib2.Request(url)
        data = urlencode(param)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, data)
        return response.read()