FROM ruby:2.6-slim

WORKDIR /srv/slate

EXPOSE 4567

COPY . /srv/slate

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        nodejs \
		python3 \
    && gem install bundler \
    && bundle install \
    && apt-get remove -y build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash", "./build.sh"]