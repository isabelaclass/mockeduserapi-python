FROM python:3.9-slim

WORKDIR /usermanagementapi

COPY requirements.txt /usermanagementapi/

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usermanagementapi/

ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
