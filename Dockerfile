FROM python:3.11
ENV FLASK_ENV=ProdConfig
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./run.py /code/run.py
COPY ./config.py /code/config.py

RUN pip install -r /code/requirements.txt

COPY ./app /code/app

CMD ["python", "run.py"]
