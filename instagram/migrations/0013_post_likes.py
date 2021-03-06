from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0012_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='instagram.Profile'),
        ),
    ]
