ARG VARIANT="3.8-slim"
FROM python:$VARIANT

RUN apt update
RUN apt install make
RUN apt-get -y install git
RUN apt-get -y install texlive
RUN apt-get install -y latexmk
RUN apt-get install -y texlive-latex-extra

RUN pip install --no-cache-dir -U sphinx && \
	pip install --no-cache-dir sphinx-rtd-theme && \
	pip install --no-cache-dir pytest

