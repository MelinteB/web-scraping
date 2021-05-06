# Generated by Django 3.1.3 on 2021-05-06 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_page', '0001_initial'),
        ('tweets', '0005_tweet_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_page.webpagead'),
        ),
    ]
