# syntax=docker/dockerfile:1

FROM python:3.9-slim
WORKDIR /app
COPY . .
COPY  pol.traineddata /usr/share/tesseract-ocr/5/tessdata/
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install -y --no-install-recommends tesseract-ocr && rm -rf /var/lib/apt/lists/*
ENV PATH="/app:${PATH}"
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
