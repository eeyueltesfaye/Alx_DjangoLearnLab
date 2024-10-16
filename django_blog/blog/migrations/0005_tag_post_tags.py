# Generated by Django 5.1.1 on 2024-09-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(related_name="posts", to="blog.tag"),
        ),
    ]
