from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20191012_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='My Bio', max_length=500),
        ),
    ]
