import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model): #so theses fields are django classes that allow the database to be created. do we need to use fields?
    def __str__(self):
    	return self.question_text
    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    	return self.choice_text

#Steps to making model changes:

#Change your models (in models.py).
#Run python manage.py makemigrations to create migrations for those changes
#Run python manage.py migrate to apply those changes to the database.