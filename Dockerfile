FROM python:3.13-slim

WORKDIR /app 

COPY BasicPythonHttpServer.py .

EXPOSE 8000

CMD ["python", "BasicPythonHttpServer.py"]


