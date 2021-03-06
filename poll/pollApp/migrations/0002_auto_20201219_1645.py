# Generated by Django 3.1.4 on 2020-12-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pollQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('numberOfOptions', models.IntegerField()),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
