from django.test import TestCase

from .models import Post

# Create your tests here.

from blog.models import Category
from django.contrib.auth.models import User

user = User.objects.get(id=1)
cat = Category.objects.all()

cat.filter(is_nav=0).delete()
