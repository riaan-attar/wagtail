# Generated by Django 4.2.1 on 2023-06-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0086_populate_grouppagepermission_permission"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="grouppagepermission",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="grouppagepermission",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("permission__isnull", False),
                    ("permission_type__isnull", False),
                    _connector="OR",
                ),
                name="permission_or_permission_type_not_null",
            ),
        ),
        migrations.AddConstraint(
            model_name="grouppagepermission",
            constraint=models.UniqueConstraint(
                fields=("group", "page", "permission"),
                name="unique_permission",
            ),
        ),
        migrations.AddConstraint(
            model_name="grouppagepermission",
            constraint=models.UniqueConstraint(
                fields=("group", "page", "permission_type"),
                name="unique_permission_type",
            ),
        ),
    ]