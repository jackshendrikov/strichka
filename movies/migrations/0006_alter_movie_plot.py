# Generated by Django 4.0.6 on 2022-09-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("movies", "0005_alter_streamingplatform_unique_together")]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="plot",
            field=models.TextField(help_text="Movie plot"),
        )
    ]
