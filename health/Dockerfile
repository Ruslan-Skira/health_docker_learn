FROM python:3.9-slim

RUN mkdir /code
WORKDIR /code

# add all files from /helth to /code
ADD .. /code

RUN pip install -r requirements.txt

CMD ["./gunicorn.sh"]

# monitoring
HEALTHCHECK --interval=1s --timeout=1s --start-perod=5s --retries=3 CMD curl -f  http://localhos/health

EXPOSE 5000:80
