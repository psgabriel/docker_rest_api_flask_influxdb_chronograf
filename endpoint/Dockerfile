FROM python

RUN pip install Flask
RUN pip install influxdb

ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["/tmp/worker.py"]