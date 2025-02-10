# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12.9-alpine3.21

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache git
RUN git clone https://github.com/spot131/pyTelegramBotAPI.git

RUN mkdir /app
RUN cp -r /pyTelegramBotAPI/* /app

WORKDIR /app

RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["python", "honest_dick_meter.py"]