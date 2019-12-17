from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.PROTECT)
    title=models.CharField(max_length=200)
    text=models.CharField(max_length=100)
    create_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        #this method will be called when author click publish button
        self.publish_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
        #eventually need to show only the approved comments

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    '''
    after creating a post and clicking post button
    where should I go...well go to post_detail view of primary key of the post
    IT HAS TO BE get_absolute_url...as django search for it
    '''

    def __str__(self):
        return self.title

class Comments(models.Model):
    post=models.ForeignKey('BLOG_APP.Post',related_name='comments',on_delete=models.PROTECT)
    #Each comment will be added to a blog application
    author=models.CharField(max_length=200)
    text=models.TextField(max_length=200)
    create_date=models.DateTimeField(default=timezone.now)
    approved_comments=models.BooleanField(default=False)

    def approve(self):
        #when approve button will be clicked this function will be called
        self.approved_comments=True
        self.save()
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
