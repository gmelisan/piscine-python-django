#!/bin/bash

rm -f db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell <<EOF
from django.contrib.auth.models import User
from deadjournal.models import Article, UserFavouriteArticle

user1 = User.objects.create_user(username='user1', password='1234')
user2 = User.objects.create_user(username='user2', password='1234')
user3 = User.objects.create_user(username='user3', password='1234')

content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
"""

a1 = Article.objects.create(title='Title1', author=user1, synopsis='Synopsis1', content=content)
a2 = Article.objects.create(title='Title2', author=user2, synopsis='Synopsis2', content=content)
a3 = Article.objects.create(title='Title3', author=user1, synopsis='Synopsis3', content=content)
a4 = Article.objects.create(title='Title4', author=user1, synopsis='Synopsis4', content=content)
a5 = Article.objects.create(title='Title5', author=user3, synopsis='Synopsis5', content=content)

fa1 = UserFavouriteArticle.objects.create(user=user1, article=a2)
fa2 = UserFavouriteArticle.objects.create(user=user1, article=a5)

EOF
