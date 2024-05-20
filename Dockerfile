FROM python:3.11

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY src/main.py /app

ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]