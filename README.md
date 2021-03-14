#### Run project with dev settings

`docker-compose build`
`docker-compose run web python manage.py migrate`
`docker-compose up`


#### Deploying Django to production
`heroku create`
`heroku config:set ALLOWED_HOSTS=YOUR_UNIQUE_URL`
`heroku config:set ALLOWED_HOSTS=glacial-brushlands-33024.herokuapp.com`
`heroku config:set DJANGO_SETTINGS_MODULE=news_develops_today.settings.prod`
`heroku config:set SECRET_KEY="ENTER YOUR KEY"`
`heroku addons:create heroku-postgresql:hobby-dev`
`git push heroku main`
`heroku ps:scale web=1`