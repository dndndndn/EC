# Generated by Django 2.1.1 on 2019-04-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('android', '0002_auto_20190414_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiongroup',
            name='tips',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='备注'),
        ),
    ]