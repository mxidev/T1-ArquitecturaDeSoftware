FROM python:3.9

RUN pip install fastapi uvicorn

WORKDIR /app
RUN mkdir -p /var/log

COPY main.py /app/main.py
COPY promtail-config.yml /etc/promtail/config.yml

RUN apt-get update && apt-get install -y wget && \
    wget https://github.com/grafana/loki/releases/download/v2.8.1/promtail-linux-amd64.zip && \
    unzip promtail-linux-amd64.zip && \
    mv promtail-linux-amd64 /usr/local/bin/promtail && \
    rm promtail-linux-amd64.zip

EXPOSE 80 9080

CMD ["sh", "-c", "promtail -config.file=/etc/promtail/config.yml & uvicorn main:app --host 0.0.0.0 --port 80"]
