FROM python:3.6-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
COPY . /app

ENV TWITTER_CONSUMER_KEY=
ENV TWITTER_CONSUMER_SECRET=
ENV TWITTER_ACCESS_TOKEN=
ENV TWITTER_ACCESS_TOKEN_SECRET=

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
