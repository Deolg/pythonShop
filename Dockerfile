FROM python:3
ADD src /src/
WORKDIR /src
ADD requirements.txt /src/
RUN pip install -r requirements.txt
