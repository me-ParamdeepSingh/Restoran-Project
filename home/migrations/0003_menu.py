# Generated by Django 4.2.2 on 2023-06-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_link_verify_link_rnd_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.TextField()),
                ('item_price', models.IntegerField()),
                ('item_image', models.ImageField(upload_to='menu_items')),
            ],
        ),
    ]
