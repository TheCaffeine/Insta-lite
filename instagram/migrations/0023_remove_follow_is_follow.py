

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0022_follow_is_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='is_follow',
        ),
    ]
