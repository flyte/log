FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1

COPY log.py /log.py

CMD [ "python", "/log.py" ]
