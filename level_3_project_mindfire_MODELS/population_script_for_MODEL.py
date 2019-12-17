import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','level_3_project_mindfire_MODELS.settings')

import django
django.setup()

from MODEL_CREATION.models import AccessRecord,WebPage,Topic

import random

from faker import Faker

fakeGen =Faker()

topics=['SEARCH','SOCIAL','MARKET','NEWS','GAMES']

def Add_Topic():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N):
    for i in range(N):
        topic_name = Add_Topic()
        url=fakeGen.url()
        date_data=fakeGen.date()
        web_name=fakeGen.company()

        #----webpage Entry
        webpg=WebPage.objects.get_or_create(topic_name=topic_name,webpage_name=web_name,url_name=url)[0]

        #---AccessRecord Entry
        acc_rec=AccessRecord.objects.get_or_create(webpage_name=webpg,date_last_accessed=date_data)[0]

if __name__ == '__main__':
    populate(5)
