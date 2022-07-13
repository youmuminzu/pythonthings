from urllib import parse
from urllib import request

from scrapy import Selector
''''''
url = "https://tophub.today/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
req = request.Request(url = url,headers = headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

# f = open('hotpoint.html',mode='r+', encoding='utf-8')
# f.write(html)
# html = f.read()
# f.close()
selector = Selector(text=html)
blocks = selector.xpath('//div[@class="cc-cd"]')
# hotlines = selector.xpath('//div[@class="cc-cd-cb-ll"]/span[@class="t"]/text()').getall()
out_put_file = open('tophub_out.txt','w',encoding='utf-8')
for block in blocks:
    lines = ''
    block_name = block.xpath('.//div[@class="cc-cd-lb"]/span/text()').get()
    print(block_name)
    lines += ('====================' + block_name + '====================' + '\n')
    block_list = block.xpath('.//div[@class="cc-cd-cb-ll"]')
    for item in block_list:
        item_value = item.xpath('.//span[@class="t"]/text()').get()
        print(item_value)
        lines += (item_value + '\n')
    out_put_file.write(lines)
    
out_put_file.close()
    
