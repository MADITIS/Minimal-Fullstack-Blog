# Generated by Django 4.2 on 2023-05-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_date_added_blog_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]