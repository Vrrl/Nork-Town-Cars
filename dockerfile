FROM python:3.10

WORKDIR /code

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

ENV DATABASE_CONNECTION_STRING=

CMD ["python", "server.py"]    