FROM python:slim-buster
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]

EXPOSE 5123