# Generated by Django 4.0.1 on 2022-06-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_alter_newsstory_options_newsstory_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='story_img',
            field=models.CharField(default='https://i.picsum.photos/id/1060/5598/3732.jpg?hmac=31kU0jp5ejnPTdEt-8tAXU5sE-buU-y1W1qk_BsiUC8', max_length=500),
        ),
    ]