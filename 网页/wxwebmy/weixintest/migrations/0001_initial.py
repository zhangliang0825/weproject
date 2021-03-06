# Generated by Django 2.0.1 on 2019-07-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cookies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'cookies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('html', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('media', models.CharField(blank=True, max_length=30, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('is_top', models.CharField(blank=True, max_length=30, null=True)),
                ('is_ori', models.CharField(blank=True, max_length=30, null=True)),
                ('datetime', models.CharField(blank=True, db_column='DATETIME', max_length=20, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Hisinfo_cx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('media', models.CharField(blank=True, max_length=30, null=True)),
                ('datetime', models.CharField(blank=True, db_column='DATETIME', max_length=20, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'hisinfo_cx',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Num',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'num',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'words',
                'managed': True,
            },
        ),
    ]
