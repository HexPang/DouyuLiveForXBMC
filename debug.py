from YYTvAPI import YYTvAPI

__author__ = 'hexpang'
helper = YYTvAPI()
result = helper.loadCategory()
for category in result:
    print category
print "Done"