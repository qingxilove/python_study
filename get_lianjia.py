#coding:utf-8
#链家爬虫，获取房源信息等

import requests
from lxml import etree

url1="http://cd.lianjia.com/ershoufang/CDQY92816359.html"
House_Number="CDQY92816359"
#房源数据链接
url2="http://cd.lianjia.com/ershoufang/comment/?hid=CDQY92816359&p=1"
#房源评论数据
header={'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Referer':'http://cd.lianjia.com/ershoufang/qingyang/',
		'Cookie':'select_city=510100; all-lj=75cfc00b9f12050e3970154c91c12727; lianjia_ssid=17f4a345-4f6f-4275-a9bc-400e00d89c70; lianjia_uuid=d799bb90-8da0-440a-ac3b-5e8c890d59ae; gr_user_id=77c29fb6-11fb-4bfd-ac12-b803f991ae0f; gr_session_id_a1a50f141657a94e=ff6fe2d4-979d-4b97-8bbe-5c001b12b8a3; _smt_uid=5818c563.2f0664b8; _ga=GA1.2.1704012507.1478018404; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; CNZZDATA1253492306=630122917-1477962902-%7C1477962902; CNZZDATA1254525948=2052545965-1477960461-%7C1477960461; CNZZDATA1255633284=675808456-1477961561-%7C1477961561; CNZZDATA1255604082=1466105392-1477962405-%7C1477962405'
		}

content=requests.get(url1,headers=header).content
root=etree.HTML(content)
# print root.xpath('//title/text()')[0]#页面标题
# print root.xpath('//div[@class="info-box left"]//text()')
data=root.xpath('//div[@class="info-box left"]//text()')
# print len(data)
# i=0
# for item in data:
# 	print str(i)+"::"+item
# 	i+=1
# price="".join(data[0:3])			#总价
# house_size=data[3]					#面积
# unit_price="".join(data[4:6])		#单价
# down_payments="".join(data[6:8])	#首付
# Monthly_payment="".join(data[8:10])	#月供
# house_type="".join(data[10:12])		#户型
# house_Orientation="".join(data[12:14])	#朝向
# floor="".join(data[14:16])				#楼层
# residence_community="".join(data[16:23])#小区
# house_year=data[23]						#建设年份
# Recent_deal=[" ".join(data[34:37])," ".join(data[37:40])," ".join(data[40:43])]

# print "面积:",house_size[1:]
# print price+'\n'+unit_price+'\n'+down_payments+'\n'+Monthly_payment+'\n'+house_type+'\n'+house_Orientation+'\n'+floor+'\n'+residence_community+'\n'+house_year
# print "最近成交："
# for item in Recent_deal:
# 	print item

# print root.xpath('//div[@id="commentsCon"]//text()')
# comments=root.xpath('//div[@id="commentsCon"]//text()')
# for item in comments:
# 	print item

s=u"1\u3001\u623f\u5c4b\u4ecb\u7ecd\uff1a\u6b64\u623f\u9762\u79ef\u662f88.06\u5e73\u7c73\u30022\u5ba42\u53851\u53a82\u536b\u3002\u5ba2\u5385\u4e3b\u5367\u90fd\u671d\u5357\u5e26\u9633\u53f0\uff0c\u5ba2\u5367\u5e26\u98d8\u7a97\uff0c\u671d\u5c0f\u533a\u91cc\u9762\u7684\n2\u3001\u88c5\u4fee\u60c5\u51b5\uff1a\u6709\u88c5\u4fee\uff0c\u623f\u4e1c\u81ea\u5df1\u5728\u4f4f\u7684\n3\u3001\u770b\u623f\u65b9\u5f0f\uff1a\u9884\u7ea6\n4\u3001\u5c0f\u533a\u4ecb\u7ecd\uff1a\u5c0f\u533a\u662f2008\u5e74\u5efa\u7684\u3002\u6709\u5730\u4e0b\u505c\u8f66\u4f4d\u30022\u68af4\u6237\uff0c\u6709\u4fdd\u5b8924\u5c0f\u65f6\u503c\u73ed\uff0c\u5fc5\u987b\u5237\u5361\u8fdb\u5165"
print s
