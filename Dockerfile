FROM python:3.6
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/flask-api/
CMD python /tmp/flask-api/main.py