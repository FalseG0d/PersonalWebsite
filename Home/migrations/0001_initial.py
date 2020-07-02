# Generated by Django 3.0.6 on 2020-07-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('logo', models.ImageField(upload_to='images')),
                ('favicon', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=100)),
                ('introduction', models.TextField()),
                ('link', models.CharField(max_length=300)),
                ('all_work', models.CharField(max_length=300)),
                ('all_podcast', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abstract', models.TextField()),
                ('link', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('icon', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('first_word', models.CharField(max_length=10)),
                ('abstract', models.TextField()),
                ('link', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(upload_to='images')),
                ('percentage', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=300)),
            ],
        ),
    ]
