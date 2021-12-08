

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0020_remove_profile_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
