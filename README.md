
build image:
```
docker build -t lalyos/lunch:v7 https://github.com/lalyos/docker-kpmg.git#master
```

start container:
```
docker run -dP -e TITLE="Kaveszumnet MOST" -e COLOR=cyan  lalyos/lunch:v7
```

build alpine image from local version:
```
docker build -f Dockerfile.alpine -t lunch:v7-alpine . 
```

build alpine image from git:
```
docker build -t lunch:v7-alpine https://github.com/lalyos/docker-kpmg.git#master
```

start anim gif cat version:
```
docker run -dP -e TITLE="2. CoffeeBreak" -e COLOR=HotPink -e BODY='<iframe src="https://giphy.com/embed/2L4rIUxrB6YUI35VYr" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cat-coffee-bring-get-me-2L4rIUxrB6YUI35VYr">via GIPHY</a></p>'  lunch:v7-alpine
```


## Volumes

```
docker run -d \
  --name mydb \
  -v vipdb:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret  postgres
```

select table
```
docker exec mydb \
  psql -U postgres -c 'select * from vip;'
```

final solution
```
docker run -d \
  --name mydb \
  -v vipdb:/var/lib/postgresql/data \
  -v $PWD/sql:/docker-entrypoint-initdb.d \
  -e POSTGRES_PASSWORD=secret  \
  postgres
```