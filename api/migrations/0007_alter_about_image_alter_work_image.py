# Generated by Django 4.1 on 2023-01-12 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_about_image_alter_work_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='トップ画像'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(blank=True, default='images/thumbnail/noImage.jpg', upload_to='images/thumbnail', verbose_name='サムネイル'),
        ),
    ]
