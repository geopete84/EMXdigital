FROM python:alpine

LABEL maintainer="George Peterson"

WORKDIR /app

COPY . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt; \
addgroup -S george && \
adduser -S george -G george; \
apk update && apk add bash vim; \
chmod a+rwx /app/app.log

USER george

EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "--log-level=debug", "--log-file=app.log"]