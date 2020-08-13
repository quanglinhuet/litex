import requests
import json
import csv
data={}
url='https://1f71593756b749fb2636693c2bebad98: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@lynk-store-p.myshopify.com/admin/api/2020-07/customers.json'
with requests.Session() as s:
    res= s.get(url)
    with open('customers.json','w',encoding='utf-8') as f:
        f.write(res.text)
    with open('customers.json','r') as r:
        data = json.load(r)
customers=data.get('customers')
keysList=list(customers[0].keys())
addressList=[]
for i in keysList:
    if 'addres' in i: 
        addressList.append(i)
        keysList.remove(i)
with open('saveCustomers.csv','w') as wFile:
    writer = csv.writer(wFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(keysList)
    for customer in customers:
        templist=[]
        for key,val in customer.items():
            if key not in addressList:
                templist.append(val)
        writer.writerow(templist)
