# Generated by Django 2.2 on 2019-04-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityentry',
            name='my_community',
            field=models.CharField(choices=[('my_community', 'This is my community'), ('proxy', 'I am creating this community on behalf of another group of people')], default='my_community', max_length=50, verbose_name='Is this your community?'),
        ),
    ]
