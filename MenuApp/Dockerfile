FROM ubuntu:latest
MAINTAINER Alex Bondar "abondar1992@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential python-mysqldb  libmysqlclient-dev
COPY . /app
WORKDIR /app
RUN pip install SQLAlchemy
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["app.py"]