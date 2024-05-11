FROM python:3.11.4
ENV PYTHONBUFFERED=1
WORKDIR /code
COPY requirements.txt .
RUN pip install -requirements.txt
COPY . .
EXPOSE 8000
CMD ["python","manage.py","runserver"]
