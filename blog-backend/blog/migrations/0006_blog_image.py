# Generated by Django 4.2 on 2023-05-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_author_blog_date_added_blog_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='media/images/default.jpg', upload_to='images/'),
        ),
    ]
