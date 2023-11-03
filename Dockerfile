FROM python:3.11-slim
WORKDIR /app
COPY ./quiz/requirements.txt .
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY quiz/ .
CMD ["gunicorn", "quiz.wsgi:application", "--bind", "0:8000" ]