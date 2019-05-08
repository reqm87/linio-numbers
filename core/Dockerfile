FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /linionumbers
WORKDIR /linionumbers
COPY requirements.txt /linionumbers/
RUN pip install -qU pip
RUN pip install -r requirements.txt
COPY . /linionumbers/
