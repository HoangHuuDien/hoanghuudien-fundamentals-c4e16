#1 Download web page
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyexcel
html_content = urlopen("http://dantri.com.vn/").read().decode('utf8')
# print(html_content)

url = "http://dantri.com.vn/"

# #1.1 Open connection
# conn = urlopen(url)
#
# # 1.2 read
#
# data = conn.read()
#
# #1.3 Decode
# html_content = data.decode('utf8')

# save html_content to file
# html_file = open("dantri.html", "wb")
# html_file.write(html_content)
# html_file.close()
#2 Check ROI (Region of Interest)

soup = BeautifulSoup(html_content, "html.parser") # xml, xhtml, html

# print(soup.prettify()) # làm cho hiển thị đẹp hơn

ul = soup.find('ul', 'ul1 ulnew') #chỉ dùng duy nhất với class ko cần class ="", find lấy 1 cái thằng đầu tiên

# print(ul.prettify())

#3 Extract info

li_list = ul.find_all("li")


datas = []
for li in li_list:
    data = {}
    a = li.h4.a
    data["title"] = a.String
    data["link"] = url + a["href"]
    datas.append(data)

pyexcel.save_as(records=datas, dest_file_name="dantri.xlsx")
# li = li_list[0]
#
# h4 = li.find('h4')
#
# print(h4)
#
# print('*' * 20)
#
# a = h4.find('a')
# for li in li_list:
#     print(li.prettify())
#     print('* ' *30)
