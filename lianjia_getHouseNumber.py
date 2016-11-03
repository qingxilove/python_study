#coding:utf-8
#获取成都主城区所有的房源编号
#锦江区：jinjiang,青羊区：qingyang,武侯区：wuhou,高新：gaoxin7,成华：chenghua,金牛：jinniu,天府新区：tianfuxinqu

import requests
import codecs
import json
import MySQLdb
from lxml import etree

zones=['jinjiang','qingyang','wuhou','gaoxin7','chenghua','jinniu','tianfuxinqu']
# zones=['jinjiang']
url="http://cd.lianjia.com/ershoufang/"
header={'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Referer':'http://cd.lianjia.com/ershoufang/qingyang/',
		'Cookie':'select_city=510100; all-lj=75cfc00b9f12050e3970154c91c12727; lianjia_ssid=17f4a345-4f6f-4275-a9bc-400e00d89c70; lianjia_uuid=d799bb90-8da0-440a-ac3b-5e8c890d59ae; gr_user_id=77c29fb6-11fb-4bfd-ac12-b803f991ae0f; gr_session_id_a1a50f141657a94e=ff6fe2d4-979d-4b97-8bbe-5c001b12b8a3; _smt_uid=5818c563.2f0664b8; _ga=GA1.2.1704012507.1478018404; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; CNZZDATA1253492306=630122917-1477962902-%7C1477962902; CNZZDATA1254525948=2052545965-1477960461-%7C1477960461; CNZZDATA1255633284=675808456-1477961561-%7C1477961561; CNZZDATA1255604082=1466105392-1477962405-%7C1477962405'
		}
conn=MySQLdb.connect(
	host='localhost',
	port=3306,
	user='root',
	passwd='admin',
	db='lianjia'
	)
#数据库连接信息，
cur=conn.cursor()
#创建数据表
cur.execute("create table if not exists houseNumber(houseID varchar(50),zone varchar(20))")

for zone in zones:
	URL=url+zone
	print URL
	content=requests.get(URL,headers=header).content
	root=etree.HTML(content)
	totalPageNum=json.loads(root.xpath("//div[@page-data]/@page-data")[0])["totalPage"]
	print totalPageNum
	for i in xrange(totalPageNum):
		URL=url+zone+'/pg'+str(i+1)+'/'
		print URL
		content=requests.get(URL,headers=header).content
		root=etree.HTML(content)
		houseNumber=root.xpath("//li/@data-id")

		# with codecs.open('/root/Python/houseNums.txt','a',encoding='utf-8') as file:
		# 	for j in xrange(len(houseNumber)):
		# 		file.write(houseNumber[j]+'\n')
		for j in xrange(len(houseNumber)):
			#插入一条数据
			cur.execute("insert into houseNumber values('%s','%s') "% (zone,houseNumber[j]))
			conn.commit()
cur.close()
conn.close()
print "work is done."
