# Generated by Django 4.1.13 on 2023-12-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('price', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
