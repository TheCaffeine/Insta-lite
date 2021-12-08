

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_auto_20191012_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
