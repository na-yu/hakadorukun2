# Generated by Django 2.2.8 on 2019-12-29 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rehearsal', '0013_auto_20191102_1207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atndchangelog',
            options={'verbose_name': '出欠の変更履歴', 'verbose_name_plural': '出欠の変更履歴'},
        ),
        migrations.AlterField(
            model_name='actor',
            name='prod_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='production.ProdUser', verbose_name='アカウント'),
        ),
    ]
