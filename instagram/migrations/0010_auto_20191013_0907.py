

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0009_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment',
        ),
    ]
