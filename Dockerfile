FROM python:3.6
ADD . /app
WORKDIR /app
ENV FLASK_APP='cli.py'
RUN pip install -r requirements.txt \
    && mkdir instance \
    && flask db upgrade \
    && flask populate-db
#RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
