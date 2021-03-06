# Generated by Django 2.2.5 on 2019-09-06 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'Low'), ('N', 'Normal'), ('U', 'Urgent')], default='N', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(help_text='Scheduled end time of the task.', null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.Owner'),
        ),
    ]
