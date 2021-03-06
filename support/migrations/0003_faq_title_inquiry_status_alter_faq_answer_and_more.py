# Generated by Django 4.0.4 on 2022-05-09 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_alter_answer_content_alter_answer_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='제목'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='status',
            field=models.CharField(choices=[('p', '문의 등록'), ('o', '접수 완료'), ('c', '답변 완료')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(verbose_name='답변'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(verbose_name='질문'),
        ),
    ]
