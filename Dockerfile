FROM python:3-alpine

RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/Europe/Paris /etc/localtime && \
    echo "Europe/Paris" >  /etc/timezone

RUN apk add --no-cache postgresql-dev gcc musl-dev

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

VOLUME /app/staticfiles

ENV DATABASE_URL postgres://postgresql:postgresql@db:5432/dashboard

EXPOSE 8000

RUN chmod +x bash/run-prod.sh

CMD /app/bash/run-prod.sh
