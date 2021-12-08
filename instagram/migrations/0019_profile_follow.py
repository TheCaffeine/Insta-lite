

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0018_auto_20191014_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
