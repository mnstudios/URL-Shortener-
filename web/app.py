
import pyshorteners as sh
import json
import os
from flask import Flask,request, jsonify
from elasticsearch import Elasticsearch

import logging
from sys import stdout

# Define logger
logger = logging.getLogger('mylogger')

logger.setLevel(logging.DEBUG) # set logger level
logFormatter = logging.Formatter\
("%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
consoleHandler = logging.StreamHandler(stdout) #set streamhandler to stdout
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

es = Elasticsearch(['elasticsearch:9200'])
index_name="url-index"



app = Flask(__name__,template_folder='template')
app.debug = True


@app.route('/create', methods=['post'])
def create():
    data = request.get_json()
    url=data["url"]
    s = sh.Shortener()
    logger.info('Data Received: "{data}"'.format(data=url))
    tiny = s.tinyurl.short(url)
    doc = {
        'url': url ,
        'tiny': tiny
    }
    res = es.index(index=index_name,body=doc)
    logger.info(res)
    es.indices.refresh(index=index_name)
    return "Request Processed.\n"


@app.route('/edit', methods=['post'])
def edit():
    data = request.get_json()
    tiny=data["tiny"]
    url=data["url"]
    s = sh.Shortener()
    logger.info(url)
    logger.info(tiny)
    tiny_new = s.tinyurl.short(url)
    logger.info(tiny_new)
    search_param = {
      'query': {
          'match': {
              'tiny': tiny
          }
        }
      }

    res = es.search(index=index_name, body=search_param)
    idd=res['hits']['hits'][0]['_id']
    logger.info(idd)
    doc = {
        'doc': {
        'url': url ,
        'tiny': tiny_new
        }
      }
    res = es.update(index=index_name, id=idd, body=doc)
    return "Request Processed.\n"

@app.route('/<string:id>', methods=['get'])
def get(id):
    logger.info(id)
    search_param = {
    'query': {
        'match': {
            '_id': id
        }
      }
    }

    res = es.search(index=index_name, body=search_param)
    data=res['hits']['hits'][0]['_source']['url']
    logger.info(data)
    return "url: "+ data


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=4001)
   
