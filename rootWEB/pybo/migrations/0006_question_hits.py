# Generated by Django 4.2 on 2023-04-12 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pybo", "0005_answer_voter_question_voter_alter_answer_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="hits",
            field=models.PositiveIntegerField(default=0, verbose_name="조회수"),
        ),
    ]
