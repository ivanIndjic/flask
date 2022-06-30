FROM python:3.8.12-bullseye
WORKDIR /app
COPY . /app
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
