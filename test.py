#coding:utf-8

import requests
import json
import codecs
from lxml import etree

# url="http://cd.lianjia.com/ershoufang/qingyang/"
InitPageNum=1
url="http://cd.lianjia.com/ershoufang/comment/?hid=CDQY92816359&p="
URL=url+str(InitPageNum)
header={'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Referer':'http://cd.lianjia.com/ershoufang/qingyang/',
		'Cookie':'select_city=510100; all-lj=75cfc00b9f12050e3970154c91c12727; lianjia_ssid=17f4a345-4f6f-4275-a9bc-400e00d89c70; lianjia_uuid=d799bb90-8da0-440a-ac3b-5e8c890d59ae; gr_user_id=77c29fb6-11fb-4bfd-ac12-b803f991ae0f; gr_session_id_a1a50f141657a94e=ff6fe2d4-979d-4b97-8bbe-5c001b12b8a3; _smt_uid=5818c563.2f0664b8; _ga=GA1.2.1704012507.1478018404; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; CNZZDATA1253492306=630122917-1477962902-%7C1477962902; CNZZDATA1254525948=2052545965-1477960461-%7C1477960461; CNZZDATA1255633284=675808456-1477961561-%7C1477961561; CNZZDATA1255604082=1466105392-1477962405-%7C1477962405'
		}
content=requests.get(URL,headers=header).content
result=json.loads(content)
# print result.keys()
# print result["totalNum"]
# # [u'itemData', u'totalNum']
# print result["itemData"][0]["Comment"]["commentContent"]

# print result["itemData"][0]["Comment"]["commentTitle"]
# print result["itemData"][0]["Comment"]["commentContent"]
# print result["itemData"][0]["Comment"]["lastModifyTime"]
totalNum=result["totalNum"]
if totalNum%3==0:
	totalPageNum=totalNum/3
else:
	totalPageNum=totalNum/3+1
lastNum=totalNum%3
if lastNum==0:
	for pageNumber in xrange(totalPageNum):
		NewUrl=url+str(pageNumber+1)
		content=requests.get(NewUrl,headers=header).content
		result=json.loads(content)
		for i in xrange(3):
			with codecs.open("/root/python/lianjia.txt","a",encoding='utf8') as file:
				file.write(result["itemData"][i]["Comment"]["commentTitle"]+'\n')
				file.write(result["itemData"][i]["Comment"]["commentContent"]+'\n')
				file.write(result["itemData"][i]["Comment"]["lastModifyTime"]+'\n')
else:
	for pageNumber in xrange(totalPageNum-1):
		NewUrl=url+str(pageNumber+1)
		print NewUrl
		content=requests.get(NewUrl,headers=header).content
		result=json.loads(content)
		for i in xrange(3):
			with codecs.open("/root/python/lianjia.txt","a",encoding='utf8') as file:
				file.write(result["itemData"][i]["Comment"]["commentTitle"]+'\n')
				file.write(result["itemData"][i]["Comment"]["commentContent"]+'\n')
				file.write(result["itemData"][i]["Comment"]["lastModifyTime"]+'\n')
	NewUrl=url+str(totalPageNum)
	print NewUrl
	content=requests.get(NewUrl,headers=header).content
	result=json.loads(content)
	for i in xrange(lastNum):
		with codecs.open("/root/python/lianjia.txt","a",encoding='utf8') as file:
			file.write(result["itemData"][i]["Comment"]["commentTitle"]+'\n')
			file.write(result["itemData"][i]["Comment"]["commentContent"]+'\n')
			file.write(result["itemData"][i]["Comment"]["lastModifyTime"]+'\n')

	# root=etree.HTML(content)
#获取房源编号，页面总数
# print root.xpath("//li/@data-id")		#获取房源编号
# print root.xpath("//div[@page-data]/@page-data")
# print json.loads(root.xpath("//div[@page-data]/@page-data")[0]).keys()
# [u'totalPage', u'curPage']
# totalPage=json.loads(root.xpath("//div[@page-data]/@page-data")[0])["totalPage"]
# print totalPage
