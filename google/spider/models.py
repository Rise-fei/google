from django.db import models

# Create your models here.



class CustLoginRecord(models.Model):
    username = models.CharField(max_length=64)
    oa_session_key = models.CharField(max_length=64)
    login_time = models.DateTimeField(auto_now_add=True)



class SearchResult(models.Model):
    name = models.CharField(max_length=64)
    website = models.CharField(max_length=512,null=True)
    email = models.CharField(max_length=128,null=True)
    type = models.CharField(max_length=512,null=True)
    address = models.CharField(max_length=128,null=True)
    phone = models.CharField(max_length=32,null=True)
    facebook = models.CharField(max_length=128,null=True)
    youtube = models.CharField(max_length=128,null=True)
    twitter = models.CharField(max_length=128,null=True)
    search_word = models.CharField(max_length=64)
    country = models.CharField(max_length=32,null=True)
    place_id = models.CharField(max_length=128,unique=True)
    td_html = models.TextField(null=True)
    status = models.IntegerField(default=0)
    update_time = models.DateTimeField(auto_now_add=True,null=True)



