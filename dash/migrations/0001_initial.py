# Generated by Django 2.0.7 on 2019-09-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('optionA', models.TextField()),
                ('optionB', models.TextField()),
                ('optionC', models.TextField()),
                ('optionD', models.TextField()),
                ('answer', models.PositiveSmallIntegerField(max_length=1)),
                ('marks', models.PositiveSmallIntegerField(max_length=1)),
            ],
        ),
    ]
