

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0019_profile_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follow',
        ),
    ]
