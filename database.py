import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")  # Update with project name
django.setup()

from food.models import Item


# print(Item.objects.all())

# a = Item(item_name="Pizza",item_desc="Cheesy Pizza",item_price=20)
# a.save()
# print(a.id)
# print(a.pk)  #Primary Key

# b = Item(item_name="Burger",item_desc="Cheesy Burger",item_price=10)
# b.save()
# print(b.id)

# print(Item.objects.all())





# from django.contrib.auth.models import User

# user = User.objects.filter(username='hani21').first()
# print(user)
# print(user.profile)
# print(user.profile.image)




# from django.contrib.auth import get_user_model
# from users.models import Profile  # or whatever model is failing

# User = get_user_model()
# user = User.objects.get(username='hani')

# Profile.objects.get_or_create(user=user)

