# Generated by Django 4.0a1 on 2021-10-04 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('NS', 'Not started'), ('PS', 'Planning stage'), ('IP', 'In progress'), ('OG', 'Ongoing'), ('AD', 'Almost Done'), ('CO', 'Completed')], default=('NS', 'Not started'), max_length=2)),
            ],
        ),
    ]
