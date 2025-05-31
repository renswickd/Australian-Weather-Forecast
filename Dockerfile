FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -e .

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["python", "app.py"]
# This Dockerfile sets up a Python environment for a Flask application.
# It installs the application dependencies and exposes port 5000 for the Flask server.