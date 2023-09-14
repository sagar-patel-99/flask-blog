FROM python:3.9-slim-buster
WORKDIR /flask_blog
COPY ./requirements.txt /flask_blog
COPY ./test_app.py /flask_blog
COPY ./app.py /flask_blog
RUN pip install -r requirements.txt
RUN python -m unittest test_app
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
