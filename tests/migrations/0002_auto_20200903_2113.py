# Generated by Django 3.0.3 on 2020-09-03 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='cd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='tests.CD'),
        ),
    ]