Some useful commands


# Create an empty data migration file:
  python manage.py makemigrations article --empty  (article - is a name of app)

# Example for the management command here: "mysite/article/management/commands/update_article_titles.py"

  python manage.py update_article_titles 1 (where 1 is article id)


# Create django file for your translations:
  django-admin makemessages -l en (en - is language)

# Create django translation file for himself according to your translations:
  python manage.py compilemessages -l en (en - is language)