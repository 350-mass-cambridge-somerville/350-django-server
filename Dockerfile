FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN mkdir /code
RUN mkdir /code/staticfiles
RUN mkdir /code/media
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/