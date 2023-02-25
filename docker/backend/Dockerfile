FROM python:3.10-alpine

ENV PYTHONPATH=/backend:${PYTHONPATH}

WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./docker/backend/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
