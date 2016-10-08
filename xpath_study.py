# coding:utf-8
# 学习xpath的使用

import requests
import re
from lxml import etree
import codecs

url="http://bbs.tianya.cn/post-worldlook-223829-2.shtml"
header={"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.6.1","Referer": "http://bbs.tianya.cn/post-worldlook-223829-1.shtml"}

req=requests.get(url,headers=header)

# print len(req.content)
tree=etree.HTML(req.content)
# print len(tree.xpath("//div[@class='bbs-content clearfix']"))
# print tree.xpath("//div[@class='bbs-content clearfix']/text()|//div[@class='bbs-content']/text()")
# with codecs.open('/root/python/tianya.txt','w','utf-8') as file:
# 	# i=0
# 	# print len(tree.xpath("//div[@_hostid='10174465']/div[@class='atl-content']/div/div[contains(@class,'bbs-content')]//text()"))
# 	for item in tree.xpath("//div[@_hostid='10174465']/div[@class='atl-content']/div/div[contains(@class,'bbs-content')]//text()"):
# 		# i +=1
# 		# print i
# 		file.write(item.strip()+'\n')

i=0
for item in tree.xpath("//div[@_hostid='10174465']/div[@class='atl-content']/div/div[contains(@class,'bbs-content')]//img"):
	if item is not None:
		i=i+1
		print "发现%d张图片"% i
# tree.xpath("//div[@_hostid='10174465']/div/div/div[contains(@class,'bbs-content')]//img[@original]/@original")
#使用此语句可以提取页面中作者发的图片地址

#使用xpath提前页面，可以比较容易地获取页面的文本，但是对于夹在正文中的图片，暂时还没有想到合适的方法来处理。即，无法实现图文混排保存。
