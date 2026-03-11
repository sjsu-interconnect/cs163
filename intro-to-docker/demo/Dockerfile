# https://fastapi.tiangolo.com/deployment/docker/#container-images

FROM python:3.9

WORKDIR /code

RUN pip install "fastapi[standard]" pydantic

COPY ./app /code/app
# local --> container

# Use port 8080
EXPOSE 8080

CMD ["fastapi", "run", "app/main.py", "--port", "8080", "--host", "0.0.0.0"]