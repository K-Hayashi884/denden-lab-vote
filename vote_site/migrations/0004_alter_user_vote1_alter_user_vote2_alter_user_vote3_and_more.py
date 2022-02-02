# Generated by Django 4.0.1 on 2022-01-31 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vote_site", "0003_alter_user_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="vote1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voter1",
                to="vote_site.lab",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="vote2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voter2",
                to="vote_site.lab",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="vote3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voter3",
                to="vote_site.lab",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="vote4",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voter4",
                to="vote_site.lab",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="vote5",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voter5",
                to="vote_site.lab",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="vote6",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voter6",
                to="vote_site.lab",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="vote7",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voter7",
                to="vote_site.lab",
            ),
        ),
    ]
