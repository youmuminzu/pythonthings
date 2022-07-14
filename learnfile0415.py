''''''
from urllib import response
import urllib.request
from wsgiref import headers
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

res = urllib.request.Request(url ="http://httpbin.org/get",headers = header)
response = urllib.request.urlopen(res)
html = response.read().decode("utf-8")
print(html)

