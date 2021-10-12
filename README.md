# URL-Shortener-
- To start containars:
 docker-compose build
 docker-compose up -d

- To create an entry
   curl localhost:4001/create -d '{"url": "https://www.youtube.com/ayushirawat/videos"}'  -H 'Content-Type: application/json'

- To get an entry
   curl localhost:4001/1

