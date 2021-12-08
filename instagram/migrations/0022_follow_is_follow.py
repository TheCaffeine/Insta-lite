

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0021_auto_20191014_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='is_follow',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
