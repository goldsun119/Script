import urllib.parse
from urllib.request import *

url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period'
decode_key = urllib.parse.unquote('aTIaQ2xH3YX61QqRvQYCrHyJtrpYj7Omi1vFIfUCIzM4908KtnLBetjsGy99joagT9qF6OdjJK1qDsoOA6xKpw%3D%3D')
#queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') : decode_key, urllib.parse.quote_plus('sido') : '서울', urllib.parse.quote_plus('gugun') : '동작구', urllib.parse.quote_plus('place') : '1', urllib.parse.quote_plus('gpsxfrom') : '129.101', urllib.parse.quote_plus('gpsyfrom') : '35.142', urllib.parse.quote_plus('gpsxto') : '129.101', urllib.parse.quote_plus('gpsyto') : '35.142', urllib.parse.quote_plus('keyword') : '', urllib.parse.quote_plus('sortStdr') : '1', urllib.parse.quote_plus('ComMsgHeader') : '', urllib.parse.quote_plus('RequestTime') : '20100810:23003422', urllib.parse.quote_plus('CallBackURI') : '', urllib.parse.quote_plus('MsgBody') : '', urllib.parse.quote_plus('realmCode') : 'A000', urllib.parse.quote_plus('cPage') : '1', urllib.parse.quote_plus('rows') : '10', urllib.parse.quote_plus('from') : '20100101', urllib.parse.quote_plus('to') : '20101201' })
queryParams = '?' + urllib.parse.urlencode({urllib.parse.quote_plus('ServiceKey') : decode_key,urllib.parse.quote_plus('ComMsgHeader') : '',urllib.parse.quote_plus('RequestTime') : '20100810:23003422',urllib.parse.quote_plus('CallBackURI') : '',urllib.parse.quote_plus('MsgBody') : '',urllib.parse.quote_plus('seq') : '12341'})

request = Request(url + queryParams)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


# url = 'http://openapi.epost.go.kr/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd'
# decode_key = urllib.parse.unquote('aTIaQ2xH3YX61QqRvQYCrHyJtrpYj7Omi1vFIfUCIzM4908KtnLBetjsGy99joagT9qF6OdjJK1qDsoOA6xKpw%3D%3D')
# queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') : decode_key, urllib.parse.quote_plus('searchSe') : 'dong', urllib.parse.quote_plus('srchwrd') : '가좌동 140-9', urllib.parse.quote_plus('countPerPage') : '10', urllib.parse.quote_plus('currentPage') : '1' })
#
# request = Request(url + queryParams)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)