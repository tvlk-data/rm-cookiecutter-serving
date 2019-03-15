FROM continuumio/miniconda3:4.5.12

RUN apt-get update -y && apt-get install -y build-essential

RUN conda install --quiet --yes python=3.6.5 && \
    conda clean --all --yes

COPY . $HOME/serving
WORKDIR $HOME/serving
RUN pip install -r requirements.txt

ENTRYPOINT [ "make" ]
CMD [ "serve" ]