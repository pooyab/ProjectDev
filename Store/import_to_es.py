#!/usr/bin/python

import time
import elastics

cars = ['']

es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
es.index(index='cars', doc_type='classifieds', body={
    'date': int(time.time()),
    'last_update': int(time.time()),
    'make': 'Toyota',
    'model': 'Camry',
    "year": '2010',
    'price': "20000",
    'color': "black",
    'zipcode':"95035",
    'short_descr': "Toyota Camry 2010, in perfect condition",
    'descr': "Moving out of country. Need to sell as soon as possible",
    'keywords': ['toyota', 'camry', 'honda']

})
