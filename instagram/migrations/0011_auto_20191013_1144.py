

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0010_auto_20191013_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='photo',
            new_name='post',
        ),
    ]
