FROM ubuntu:latest 
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app/app.py"]
EXPOSE 4001
