__author__ = 'hexpang'
#import DouyuAPI
from APIHelper import APIHelper
class YYTvAPI:
    def __init__(self):
        APIHelper.__init__()
        self.baseUrl = "http://api.douyutv.com/api/client"

    def request(self, action, param=None):
        reqUrl = self.baseUrl + "/" + action
        return APIHelper.request(self,reqUrl,param)