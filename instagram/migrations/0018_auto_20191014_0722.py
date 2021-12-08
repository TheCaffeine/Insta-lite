

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0017_auto_20191014_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follow',
            new_name='follower',
        ),
    ]
