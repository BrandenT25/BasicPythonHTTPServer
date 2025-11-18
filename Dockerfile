FROM python:3.13-slim

WORKDIR /app 

COPY BasicPythonHttpServer.py .

COPY static ./static/

EXPOSE 8000

CMD ["python","-u", "BasicPythonHttpServer.py"]


