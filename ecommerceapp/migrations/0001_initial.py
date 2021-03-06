# Generated by Django 3.1 on 2021-08-02 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_tag', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('imageUrl', models.URLField()),
                ('in_stock', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
