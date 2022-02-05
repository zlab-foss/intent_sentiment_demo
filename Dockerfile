FROM python:3.8-slim-buster

LABEL maintainer="Sina Zamani <sinazamani920@gmail.com>"

RUN apt-get update && \
    pip install --upgrade pip

WORKDIR /usr/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r /usr/app/requirements.txt

COPY . .

CMD ["uvicorn","--host", "0.0.0.0","--port","8006","src.web_service:app"]
