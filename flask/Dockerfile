FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y -q python3 python3-pip

RUN pip install flask==2.1.2

WORKDIR /app

COPY . /app

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python3"]

CMD ["app.py"]