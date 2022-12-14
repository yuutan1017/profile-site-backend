from django.db import models


class About(models.Model):
  image = models.ImageField(upload_to='media/thumbnail/')

  def __str__(self):
      return self.image


class Skills(model.Model):
  title = models.CharField(max_length=50)
  color_code = models.CharField(max_length=20)
  description = models.TextField(max_length=255)

  def __str__(self):
    return self.title


class Works(model.Model):
  image = models.ImageField(upload_to='media/thumbnail/')
  title = models.CharField(max_length=50)
  description = models.TextField()
  href = model.models.URLField(max_length=200, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title
  
