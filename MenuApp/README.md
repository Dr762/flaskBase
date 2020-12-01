# Menu

A small application showing a menu from database.

Access via localhost:7000


## Build and run

1. Run mysql
2. Create database using db_setup.py script

### Local Run

- Install all dependencies via pip.
- Run ``` python app.py```

### Build Docker image

```
docker build -t <image-tag>  .

docker run -d -p 7000:<local-port> <image-tag>

```
