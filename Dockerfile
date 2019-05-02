FROM python:3.6
ADD . /app
WORKDIR /app
#RUN "pip install -r requiriments.txt \
#    && mkdir instance \
#    && flask db upgrade \
#    && export FLASK_APP=cli.py flask populate-db"
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
