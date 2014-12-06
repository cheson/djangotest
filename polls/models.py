import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model): #so theses fields are django classes that allow the database to be created. do we need to use fields?
    def __str__(self):
    	return self.question_text

    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self):
    	return self.choice_text

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

#Steps to making model changes:

#Change your models (in models.py).
#Run python manage.py makemigrations to create migrations for those changes
#Run python manage.py migrate to apply those changes to the database.