# pull official base image
FROM python:3.9.0-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
&& apt-get install gcc postgresql postgresql-contrib libpq-dev python3-dev curl netcat zsh git -y \
&& apt-get clean

# set work directory
WORKDIR /app
COPY ./requirements ./requirements
RUN pip install -r requirements/dev-requirements.txt
# zsh config
RUN curl -L https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh | bash
# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

COPY . /app/
RUN chmod +x /app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
