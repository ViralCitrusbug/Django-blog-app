# Generated by Django 3.2.5 on 2022-02-17 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0028_auto_20220217_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content_p1',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_image_1',
            new_name='post_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_p2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_p3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_image_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_image_3',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
