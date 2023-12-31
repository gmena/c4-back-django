# Generated by Django 4.2.6 on 2023-10-25 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_player', models.IntegerField(default=1)),
                ('winner', models.IntegerField(default=None, null=True)),
                ('board', models.JSONField(max_length=200)),
            ],
        ),
    ]
