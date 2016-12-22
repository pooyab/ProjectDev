#! /usr/bin/python

import json,time,elasticsearch,random
es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
makes = []
colors = ['white','black','blue','yellow','green','red','gray','darkblue']

def insert_into_es(es,data):
    es.index(index='cars', doc_type='classifieds', body=data )



with open('./CarModels.json') as data_file:
    data = json.loads(data_file.read())

for d in data:
    makes.append(d['title'])
    make = d.get('title')
    m = len(d.get('models'))
    for i in range(0,m):
        model = d.get('models')[i].get('title')
        publish_time = int(time.time() - random.randint(0,100000))
        update_time = publish_time + random.randint(0,10000)
        year = random.randint(1970, 2016)
        price = random.randint(1000, 100000)
        data = {}
        data['date'] = publish_time
        data['last_update'] = update_time
        data['make'] = make
        data['model'] = model.replace(' ','').strip('-')
        if model.find('Other') >= 0: continue
        data['year'] = year
        data['price'] = price
        data['color'] = colors[random.randint(0, (len(colors)-1))]
        data['zipcode'] = random.randint(9200, 9700)
        data['short_descr'] = "%s %s %s, in perfect condition, price %s" % (make,model,year,price)
        data['descr'] = "%s %s year %s For sale. Price: %s. \n Moving out of country. Need to sell as soon as possible" % (make,model,year,price)
        data['keywords'] = "%s, %s" % (make, model)
        print json.dumps(data,encoding='utf8')
        insert_into_es(es,data)




