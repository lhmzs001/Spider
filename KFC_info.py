# encoding:UTF-8
# @Author: wangzi
import requests
import time
import json


keyword = input('请输入要查的名字：')
for i in range(1,3):
    data = {
        'cname':'' ,
        'pid': '',
        'keyword': keyword,
        'pageIndex': i,
        'pageSize': 10,
    }
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    print('正在打印第{}页内容'.format(i))
    time.sleep(1)
    res = requests.post(url,data=data).text
    rr = json.loads(res)
    # print(rr)
    # print(len(rr))
    # print(rr.get('Table1')[0].get('storeName'))
    for name in rr.get('Table1'):
        info= {}
        kfc_name = name.get('storeName')
        kfc_addr = name.get('addressDetail')
        info['kfc_name'] = kfc_name
        info['kfc_addr'] = kfc_addr
        print(info)
        f = open('KFC.json','a',encoding='utf-8')
        f.write(json.dumps(info,ensure_ascii=False)+'\n')