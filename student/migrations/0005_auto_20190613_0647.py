# Generated by Django 2.2.2 on 2019-06-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190612_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Foo',
        ),
    ]
