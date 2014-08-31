# -*- coding: utf-8 -*-
__author__ = 'hexpang'
import APIHelper


class DouyuAPI(APIHelper.APIHelper):
    def __init__(self):
        APIHelper.APIHelper.__init__(self)

    def loadCategory(self):
        return self.request("game")

    def loadRooms(self, cateId, offset=0, limit=10):
        return self.request("live/" + cateId, {"offset": str(offset), "limit": str(limit)})

    def loadRoom(self,roomId):
        return self.request("room/" + roomId)