FROM python:3.10

EXPOSE 80

COPY ./requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]