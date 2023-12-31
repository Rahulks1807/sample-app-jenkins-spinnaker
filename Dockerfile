FROM python:3.7-alpine3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["/app/app.py"]
