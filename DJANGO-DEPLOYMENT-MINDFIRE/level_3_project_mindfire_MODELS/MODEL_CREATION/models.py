from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.topic_name


class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.PROTECT)
    webpage_name=models.CharField(max_length=264,unique=True)
    url_name=models.URLField(unique=True)

    def __str__(self):
        return self.webpage_name

class AccessRecord(models.Model):
    webpage_name=models.ForeignKey(WebPage,on_delete=models.PROTECT)
    date_last_accessed=models.DateField()

    def __str__(self):
        return str(self.date)
