# https://www.youtube.com/watch?v=bi0cKgmRuiA&t=162s

# Dockerfile, Image, Container

# Dockerfile is a blueprint for building images.
# Image is a template for running containers.
# Container is the actual running process where we've got our packaged project.

FROM python:3.11

ADD main.py .

RUN pip install requests beautifulsoup4

CMD [ "python", "./main.py" ]




# EXAMPLE DOCKERFILE FOR THE WEB APP FROM SECOND EXAMPLE IN THIS YOUTUBE
# https://www.youtube.com/watch?v=bi0cKgmRuiA&t=162s

# FROM python:3.11

# WORKDIR /fastapi-app

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY ./app ./app

# CMD ["python", "./app/main.py"]