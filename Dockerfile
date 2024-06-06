FROM python:3.10.14-alpine3.19

EXPOSE 1993

# work directory
WORKDIR /code

# dependencies
COPY ./requirements.txt /code/requirements.txt

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# app files
COPY . /code

# running command
CMD ["uvicorn", "main:api", "--host", "127.0.0.1", "--port", "1993"]