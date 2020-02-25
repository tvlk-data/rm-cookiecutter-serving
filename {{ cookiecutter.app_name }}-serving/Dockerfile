FROM python:3.6.9-slim

RUN apt-get update && apt-get install -y \
    make \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . $HOME/serving
WORKDIR $HOME/serving
RUN pip install -r requirements.txt

ENTRYPOINT [ "make" ]
CMD [ "serve" ]