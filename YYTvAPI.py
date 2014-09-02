__author__ = 'hexpang'
#import DouyuAPI
from APIHelper import APIHelper
class YYTvAPI(APIHelper):
    def __init__(self):
        self.baseUrl = "http://m.live.yy.com/api/"

    def request(self, action, param=None, name="data"):
        result = APIHelper.request(self, action, param)
        if name is None:
            return result
        return result[name]

    def loadCategory(self):
        return self.request("game")

    def loadRooms(self, gameId, page=1):
        return self.request("game", {"gameId": gameId,"page":page})

    def liveInfo(self, liveUID):
        #liveinfo?uid=310295391
        return self.request("liveinfo",{"uid":liveUID},"info")

    def liveData(self, liveUID):
        #http://yy.com/get-data/574646677?type=json
        data = self.request()