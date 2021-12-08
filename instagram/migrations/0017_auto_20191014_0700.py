from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0016_auto_20191014_0647'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follows',
            new_name='Follow',
        ),
    ]
