FROM python

WORKDIR /Course_docker/

COPY requirements.txt /Course_docker/

RUN pip install -r requirements.txt

