# Generated by Django 4.1 on 2023-01-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_skill_description_skill_detail_delete_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill_description',
            name='category',
            field=models.CharField(choices=[(1, 'Front End'), (2, 'Back End'), (3, 'Others')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='skill_detail',
            name='category',
            field=models.CharField(choices=[(1, 'Front End'), (2, 'Back End'), (3, 'Others')], default='1', max_length=1),
        ),
    ]
