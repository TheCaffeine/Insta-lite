

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0014_auto_20191013_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
