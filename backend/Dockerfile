FROM python:3.11-buster

ARG DB_URL
ENV DB_URL=$DB_URL

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . /app

RUN pip install --upgrade pip build hatchling
RUN pip install .

CMD uvicorn etherealink.main:app --host 0.0.0.0 --port 5000