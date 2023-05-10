FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

RUN python vk_internship/manage.py makemigrations
RUN python vk_internship/manage.py migrate

CMD ["python", "vk_internship/manage.py", "runserver", "0.0.0.0:8000"]