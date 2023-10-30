# EXAMPLE DOCKERFILE FOR THE WEB APP FROM SECOND EXAMPLE IN THIS YOUTUBE
# https://www.youtube.com/watch?v=bi0cKgmRuiA&t=162s

FROM python:3.11

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]


# runs on Docker
# but instead of a default link (0.0.0.0:8000) that will be given for a click
# change browser address to either:
# localhost:8000
# OR
# 127.0.0.1:8000
# then also try
# either of the 2 above ./items/5 (or any other number)