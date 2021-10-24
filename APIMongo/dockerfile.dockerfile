FROM python:3.9-slim
COPY . .
WORKDIR /app
EXPOSE 8002:8002
RUN pip3 install -r requirements.txt
CMD [ "python3", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8002", "--reload" ]