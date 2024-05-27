FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
