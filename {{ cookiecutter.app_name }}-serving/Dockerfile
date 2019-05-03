FROM continuumio/miniconda3:4.5.12

RUN apt-get update -y && apt-get install -y build-essential

RUN conda install --quiet --yes python=3.6.5 && \
    conda clean --all --yes

WORKDIR $HOME/serving

COPY requirements.txt $HOME/serving
RUN pip install -r requirements.txt

COPY . $HOME/serving

ENTRYPOINT [ "make" ]
CMD [ "serve" ]