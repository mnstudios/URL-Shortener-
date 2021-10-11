FROM ubuntu:latest 
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN pip install --upgrade pip
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN chmod +x app.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
EXPOSE 4001
