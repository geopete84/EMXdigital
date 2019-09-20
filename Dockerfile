FROM python:alpine

LABEL maintainer="George Peterson"

WORKDIR /app

COPY . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt; \
addgroup -S george && \
adduser -S george -G george; \
export FLASK_ENV=production \
apk update && apk add bash


USER george

EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]