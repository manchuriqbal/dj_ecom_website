# Generated by Django 4.2.6 on 2023-10-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_category_slug_alter_category_title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="slider",
            name="title2",
            field=models.CharField(default="Lookbook.", max_length=50),
        ),
    ]
