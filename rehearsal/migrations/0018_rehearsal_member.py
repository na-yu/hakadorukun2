# Generated by Django 3.2.7 on 2021-09-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehearsal', '0017_auto_20210909_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='rehearsal',
            name='member',
            field=models.TextField(blank=True, verbose_name='担当'),
        ),
    ]
