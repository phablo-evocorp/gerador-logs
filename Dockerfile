FROM python:3.10-alpine

WORKDIR /app
COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "app.py", "--debug", "run", "--host=0.0.0.0" ]
