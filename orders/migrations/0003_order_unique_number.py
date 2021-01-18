# Generated by Django 2.2.1 on 2021-01-12 15:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210112_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='unique_number',
            field=models.UUIDField(default=uuid.UUID('45903fb8-2fac-42a3-a6f6-2698fd43936a'), editable=False),
        ),
    ]