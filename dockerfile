FROM python:3.12-slim

WORKDIR /autodata
COPY requirements.txt /autodata/

RUN pip install --upgrade pip
RUN pip install -r /autodata/requirements.txt

COPY manage.py /autodata/
COPY . /autodata/


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
