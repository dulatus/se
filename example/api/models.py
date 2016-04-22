from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followees', symmetrical=False)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)


class Photo(models.Model):
    post = models.ForeignKey(Post, related_name='photos')
    image = models.ImageField(upload_to="%Y/%m/%d")
class University(models.Model):
	name = models.CharField(max_length=100);
	city = models.CharField(max_length=100);
	logo = models.ForeignKey(Photo, related_name = 'universities')
class Man(models.Model):
	username = models.CharField(max_length = 50)
	name = models.CharField(max_length= 50)
	surname  = models.CharField(max_length=50)
	university = models.ForeignKey(University, related_name = 'mans')
class ContentCategory(models.Model):
	category_name = models.CharField(max_length = 50)

class Review(models.Model):
	subject = models.ForeignKey(University,related_name = 'reviews')
	data = models.CharField(max_length=600)
	thumb = models.CharField(max_length = 100)
	author = models.ForeignKey(Photo, related_name = 'reviews')
class Content(models.Model):
	content = models.CharField(max_length=250)
	photo = models.ForeignKey(Photo,)
	category = models.ForeignKey(ContentCategory, related_name ='contents')
class Faculties(models.Model):
	content = models.CharField(max_length = 50)
