# -*- coding: utf-8 -*-
__author__ = 'hexpang'
import APIHelper


class DouyuAPI(APIHelper.APIHelper):
    def __init__(self):
        APIHelper.APIHelper.__init__(self)
        self.baseUrl = "http://api.douyutv.com/api/client"
        self.client_sys = "android"

    def request(self, action, param=None):
        reqUrl = self.baseUrl + "/" + action
        reqUrl = reqUrl + "?" + "client_sys=" + self.client_sys
        return APIHelper.APIHelper.request(self, reqUrl, param)

    def loadCategory(self):
        return self.request("game")

    def loadRooms(self, cateId, offset=0, limit=10):
        return self.request("live/" + cateId, {"offset": str(offset), "limit": str(limit)})

    def loadRoom(self,roomId):
        return self.request("room/" + roomId)

    def loadLive(self,offset=0,limit=10):
        return self.request("live", {"offset": str(offset), "limit": str(limit)})