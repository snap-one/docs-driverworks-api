FROM ruby:2.5

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock ./

RUN apt-get update -qq
RUN apt-get install -y nodejs

RUN gem update --system
RUN gem install bundler -v 2.0.1
RUN bundle install

COPY . .

CMD ["bundle", "exec", "middleman", "build", "--clean", "--verbose"]