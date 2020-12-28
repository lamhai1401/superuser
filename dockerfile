FROM python:3.9.0-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    SECRET_KEY=secret \
    DEBUG=True \
    DB_CONNECTION=mysql://username:password@127.0.0.1:3306/superuser \
    HOST=127.0.0.1 \
    PORT=3306 \
    USER=username \
    PWD=password \
    DB=superuser \
    SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7 \
    ALGORITHM=HS256 \
    ACCESS_TOKEN_EXPIRE_MINUTES=30

# RUN pip install poetry
# RUN poetry completions bash > /etc/bash_completion.d/poetry.bash-completion

WORKDIR /code

# Creating folders, and files for a project:
COPY . /code/

# Add docker-compose-wait tool -------------------
# ENV WAIT_VERSION 2.7.2
# ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
# RUN chmod +x /wait

# ADD . /code/
# RUN chmod +x /code
# WORKDIR /code
RUN pip3 install -r requirements.txt

# CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port ", "8000", "--reload" ]