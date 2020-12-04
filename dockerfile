FROM python:3.9.0-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN pip install poetry
RUN poetry completions bash > /etc/bash_completion.d/poetry.bash-completion

WORKDIR /code

# Creating folders, and files for a project:
COPY . /code/

RUN pip3 install -r requirements.txt