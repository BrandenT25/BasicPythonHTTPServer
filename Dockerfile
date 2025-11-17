FROM python:3.13-slim

WORKDIR . 

COPY BasicPythonHttpServer.py .

EXPOSE 8000

CMD ["python", "BasicPythonHttpServer"]


