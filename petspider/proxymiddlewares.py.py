# -*- coding: utf-8 -*-  
import random, base64  
  
  
class ProxyMiddleware(object):  
  
    proxyList = [
        '120.132.71.212:80','61.143.228.162:3128','119.90.63.3:3128'      
        ]  

    def process_request(self, request, spider):  
        # Set the location of the proxy  
        pro_adr = random.choice(self.proxyList)  
        print("USE PROXY -> " + pro_adr)  
        request.meta['proxy'] = "http://" + pro_adr  