import urllib2
import json


class APIHelper:
    def __init__(self):
        self.baseUrl = "http://api.douyutv.com/api/client"
        self.client_sys = "android"

    def request(self, action, param=None):
        reqUrl = self.baseUrl + "/" + action
        reqUrl = reqUrl + "?" + "client_sys=" + self.client_sys
        if param != None:
            for k, v in enumerate(param):
                reqUrl = reqUrl + "&" + v + "=" + param[v]
        print(reqUrl)
        try:
            response = urllib2.urlopen(reqUrl).read()
        except Exception, e:
            print "Error:" + e
        # print response
        jsonObject = json.loads(response)
        data = jsonObject["data"]
        return data