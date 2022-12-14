# Generated by Django 4.1 on 2023-01-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_skill_description_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, default='images/noImage.jpg', upload_to='images/', verbose_name='トップ画像'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(blank=True, default='images/noImage.jpg', upload_to='images/', verbose_name='サムネイル'),
        ),
    ]
