# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:05:54 2019

@author: Rodrigo
"""

import Algorithmia
import requests
from recursivejson import extract_values
import os

ask = input('digita a personalidade que vc quer postar: ')
client = Algorithmia.client('simtcMfVcIi2EcFstBQAJlyiiKe1')
algo = client.algo('shashankgutha/WebsiteLinksRecommenderForkeywords/1.0.1')
algo.set_options(timeout=300) # optional
print (algo.pipe(ask).result[0]['abstract'] + ' know more in '  + algo.pipe(ask).result[0]['url'] )
text = (algo.pipe(ask).result[0]['abstract'] + ' know more in '  + algo.pipe(ask).result[0]['url'])

name = ask.replace(" ", "+")

response = requests.get('https://www.googleapis.com/customsearch/v1?q='+name+'&cx=007669701712061955482%3A25-pzkhbozk&imgColorType=color&imgSize=huge&fields=items%2Fpagemap&key=AIzaSyABHcWGtmCA41U3jZAuVmBWqoKGH2cUaKA')

data =  extract_values(response.json(), 'src')
print(data[0])

input = {
  "image": data[0],
  "resize": 600
}
client = Algorithmia.client('simtcMfVcIi2EcFstBQAJlyiiKe1')
algo = client.algo('util/SmartImageDownloader/0.2.18')
algo.set_options(timeout=300) # optional
save = algo.pipe(input).result
save = save['savePath']
localAbsPath = client.file(str(save[0])).getFile().name

print("start cmd /c instapy -u jiujitsu_fighters -p rod@1220 -f " +  localAbsPath + " -t "  + text)

os.system("start cmd /c instapy -u jiujitsu_fighters -p rod@1220 -f " +  localAbsPath + " -t "  +  text)


