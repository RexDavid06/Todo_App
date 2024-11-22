# Generated by Django 5.1.1 on 2024-11-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]