FROM python:3.9
RUN mkdir -p /opt/code && mkdir /opt/logs
ADD ./requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code/
RUN pip install -r requirements.txt
ADD . /opt/code
ENV FLASK_APP takehomeapi/wsgi.py
ENV FLASK_DEBUG 1
RUN python /opt/code/setup.py develop
EXPOSE 8080
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]
