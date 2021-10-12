# remarque wait for elastic search node to be available
 curl localhost:9200/_cat/health

# URL-Shortener-
- To start containars:
 docker-compose build
 docker-compose up -d


- To create an entry
   curl localhost:4001/create -d '{"url": "https://www.youtube.com/ayushirawat/videos"}'  -H 'Content-Type: application/json'

- List index document
  curl "localhost:9200/url-index/_search?pretty" -H 'Content-Type: application/json'  -d '{    "query": {"match_all": {}}} '

- get an _id from the list

- To get an entry
   curl localhost:4001/<your _id>




#  technical enhancement 
architecture mvc
swagger doc
add app volume
add execptions

