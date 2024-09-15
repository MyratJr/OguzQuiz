# Generated by Django 5.1.1 on 2024-09-07 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Quiz', '0002_delete_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=555)),
                ('answer_a', models.CharField(max_length=55)),
                ('a_is_correct', models.BooleanField(default=False)),
                ('answer_b', models.CharField(max_length=55)),
                ('b_is_correct', models.BooleanField(default=False)),
                ('answer_c', models.CharField(max_length=55)),
                ('c_is_correct', models.BooleanField(default=False)),
                ('answer_d', models.CharField(max_length=55)),
                ('d_is_correct', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='Quiz.quizgroup')),
            ],
        ),
    ]
