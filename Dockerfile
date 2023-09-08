FROM python

WORKDIR /Course_docker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

