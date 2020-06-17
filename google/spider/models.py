from django.db import models

# Create your models here.



class CustLoginRecord(models.Model):
    username = models.CharField(max_length=64)
    oa_session_key = models.CharField(max_length=64)
    login_time = models.DateTimeField(auto_now_add=True)



class SearchResult(models.Model):
    name = models.CharField(max_length=64)
    website = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    type = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    facebook = models.CharField(max_length=64)
    youtube = models.CharField(max_length=64)
    twitter = models.CharField(max_length=64)
    search_word = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
    place_id = models.CharField(max_length=128)


