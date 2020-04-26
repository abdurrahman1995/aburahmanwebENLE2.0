from django.db import models

class Adusert(models.Model):
    aduid = models.CharField(max_length=20)
    aduname = models.CharField(max_length=100)

    class Meta:
        db_table="adusert"

class User_Admin(models.Model):
    ad_id = models.AutoField(db_column='ad_id', primary_key=True)
    ad_First_name = models.CharField(max_length=100)
    ad_Lirst_name = models.CharField(max_length=100)
    ad_NIC = models.CharField(max_length=10)
    ad_Email = models.EmailField()
    ad_User_name = models.CharField(max_length=100)
    ad_Password = models.CharField(max_length=100)
    class Meta:
        db_table = "user_admin"
