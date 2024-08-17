FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 3001

ARG IMAGE_TAG
ENV IMAGE_TAG=$IMAGE_TAG

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3001"]
