# Generated by Django 2.2.6 on 2019-10-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehearsal', '0011_auto_20191005_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['sortkey'], 'verbose_name': '登場人物', 'verbose_name_plural': '登場人物'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'ordering': ['name'], 'verbose_name': '稽古場の施設', 'verbose_name_plural': '稽古場の施設'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['facility__name', 'room_name'], 'verbose_name': '稽古場', 'verbose_name_plural': '稽古場'},
        ),
        migrations.AlterModelOptions(
            name='rehearsal',
            options={'ordering': ['date', 'start_time'], 'verbose_name': '稽古のコマ', 'verbose_name_plural': '稽古のコマ'},
        ),
        migrations.AlterModelOptions(
            name='scene',
            options={'ordering': ['sortkey'], 'verbose_name': 'シーン', 'verbose_name_plural': 'シーン'},
        ),
        migrations.AlterField(
            model_name='scene',
            name='priority',
            field=models.IntegerField(choices=[(1, '1 (最高)'), (2, '2 (高)'), (3, '3'), (4, '4 (低)'), (5, '5 (最低)')], default=3, verbose_name='優先度'),
        ),
    ]
