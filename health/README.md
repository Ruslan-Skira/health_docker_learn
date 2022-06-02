docker image build -t health .
docker container run --name health-flask --publish 5000:80 -d health
you could use --rm tag. 

docker cp healthh-flask /code/text.txt