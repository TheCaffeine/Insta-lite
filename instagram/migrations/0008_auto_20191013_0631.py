from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0007_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
