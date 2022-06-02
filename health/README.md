docker image build -t health .
docker container run --name health-flask --publish 5000:80 -d health
you could use --rm tag. 

docker cp healthh-flask /code/text.tx

tutorials. 
    https://github.com/wagnerdelima/docker-handson
https://slides.com/wagnerdelima/docker-hands-on#/1
