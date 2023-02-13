FROM python:3.9

ENV PYTHONUNBUFFERED=1


WORKDIR /usr/src/app
COPY . . 

RUN pip install --upgrade pip && pip3 install -r requirements.txt


CMD ["python3", "main.py"]