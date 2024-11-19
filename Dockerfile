FROM python:3.11-slim
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
WORKDIR /fastapi
COPY . /fastapi/
CMD ["python3", "src/app.py"]