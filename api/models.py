from django.db import models


class About(models.Model):
  image = models.ImageField(upload_to='images/', verbose_name='トップ画像')
  text = models.CharField(max_length=255)

  def __str__(self):
    return "トップ画像"


class Skill(models.Model):
  title = models.CharField('タイトル', max_length=50)
  color_code = models.CharField('カラーコード', max_length=20)

  def __str__(self):
    return self.title


class Work(models.Model):
  image = models.ImageField(upload_to='images', verbose_name='サムネイル', blank=True, default='images/noImage.jpg')
  title = models.CharField('タイトル', max_length=50)
  description = models.TextField('本文')
  url = models.URLField('URL', max_length=200, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title
  
