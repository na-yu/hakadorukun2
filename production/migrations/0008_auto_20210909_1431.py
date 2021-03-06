# Generated by Django 3.2.7 on 2021-09-09 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('production', '0007_auto_20210905_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitation',
            options={'ordering': ['exp_dt'], 'verbose_name': '課題への招待', 'verbose_name_plural': '課題への招待'},
        ),
        migrations.AlterModelOptions(
            name='production',
            options={'verbose_name': '課題', 'verbose_name_plural': '課題'},
        ),
        migrations.AlterModelOptions(
            name='produser',
            options={'verbose_name': '担当', 'verbose_name_plural': '担当'},
        ),
        migrations.AlterField(
            model_name='invitation',
            name='production',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.production', verbose_name='課題'),
        ),
        migrations.AlterField(
            model_name='production',
            name='name',
            field=models.CharField(max_length=50, verbose_name='課題'),
        ),
        migrations.AlterField(
            model_name='produser',
            name='production',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.production', verbose_name='課題'),
        ),
        migrations.AlterField(
            model_name='produser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='担当'),
        ),
    ]
