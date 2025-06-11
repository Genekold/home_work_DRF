FROM python:3.12

WORKDIR /lms

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]