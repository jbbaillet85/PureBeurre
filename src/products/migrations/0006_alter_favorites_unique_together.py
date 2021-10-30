# Generated by Django 3.2.7 on 2021-10-14 10:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20211014_1126'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together={('user_id', 'product_id')},
        ),
    ]