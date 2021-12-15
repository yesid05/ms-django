FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD . ./
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python manage.py runserver 0.0.0.0:$PORT