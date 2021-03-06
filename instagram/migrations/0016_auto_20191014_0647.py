

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0015_post_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='instagram.Profile')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='instagram.Profile')),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pk']},
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
