
build image:
```
docker build -t lalyos/lunch:v7 https://github.com/lalyos/docker-kpmg.git#master
```

start container:
```
docker run -dP -e TITLE="Kaveszumnet MOST" -e COLOR=cyan  lalyos/lunch:v7
```

build alpine image:
```
docker build -f Dockerfile.alpine -t lunch:v7-alpine . 
```