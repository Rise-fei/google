from django.db import models

# Create your models here.



class CustLoginRecord(models.Model):
    username = models.CharField(max_length=64)
    oa_session_key = models.CharField(max_length=64)
    login_time = models.DateTimeField(auto_now_add=True)



