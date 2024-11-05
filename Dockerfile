
FROM python:3.6-slim-buster

ENV DD_SERVICE="alien"
ENV DD_ENV="dev"
ENV DD_VERSION="0.1.0"

LABEL com.datadoghq.tags.service="alien"
LABEL com.datadoghq.tags.env="dev"
LABEL com.datadoghq.tags.version="0.1.0"

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD [ "ddtrace-run", "flask", "run", "--host=0.0.0.0", "--port=4000"]
