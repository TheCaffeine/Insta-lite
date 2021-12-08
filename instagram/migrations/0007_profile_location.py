from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
