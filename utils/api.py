import requests
import re
import json
import time



def search(keywords, max_results= 10):
    url = 'https://duckduckgo.com/';
    img_list = []
    list_size =  max_results -1
    
    params = {
    	'q': keywords,
    };



    #   First make a request to above URL, and parse out the 'vqd'
    #   This is a special token, which should be used in the subsequent request
    res = requests.post(url, data=params)
    searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M|re.I);

    if not searchObj:

        return -1;



    headers = {
        'authority': 'duckduckgo.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-dest': 'empty',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://duckduckgo.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = (
        ('l', 'us-en'),
        ('o', 'json'),
        ('q', keywords),
        ('vqd', searchObj.group(1)),
        ('f', ',,,'),
        ('p', '1'),
        ('v7exp', 'a'),
    )

    requestUrl = url + "i.js";



    while True:
        while True:
            try:
                res = requests.get(requestUrl, headers=headers, params=params);
                data = json.loads(res.text);
                break;
            except ValueError as e:

                time.sleep(5);
                continue;



        if list_size < max_results:
            img_list += data["results"] 
        else: break
        
        
        if "next" not in data:

            exit(0);
            
        list_size = len(img_list)

        requestUrl = url + data["next"];
        
        return img_list[0: max_results]
        
if __name__ == "__main__":
    for data in search("bees",20):
        print(data["image"])