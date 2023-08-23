from django.db import models


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", height_field=40, width_field=50
    )
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    
    class  Meta:
        db_table = 'users'
        

    def __str__(self):
        return self.email
