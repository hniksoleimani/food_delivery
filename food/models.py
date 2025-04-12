from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    
    
    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Price = models.IntegerField()
    Image = models.CharField(max_length=500, default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")


    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})