# Generated by Django 4.1.1 on 2022-09-29 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(choices=[('CLEANER', 'Техничка'), ('COOK', 'Повар'), ('SEW', 'Швея'), ('PU_WORKER', 'Работник ПУ'), ('EVA_WORKER', 'Работник ЭВА'), ('HANDMAKER', 'Работник')], max_length=255, verbose_name='Должность')),
                ('working_day', models.PositiveSmallIntegerField(verbose_name='Рабочие дни')),
                ('actual_day', models.PositiveSmallIntegerField(verbose_name='Фактически отработанные дни')),
                ('social_salary', models.PositiveSmallIntegerField(verbose_name='Оклад СФ')),
                ('debt', models.PositiveSmallIntegerField(verbose_name='Задолжность')),
                ('actual_salary', models.PositiveSmallIntegerField(verbose_name='Фактически оклад')),
                ('social_fund', models.PositiveSmallIntegerField(verbose_name='Соц.Фонд')),
                ('employer_social_fund', models.PositiveSmallIntegerField(verbose_name='Работодатель СФ')),
                ('accrued_salary', models.PositiveSmallIntegerField(verbose_name='Оклад по начислениям')),
                ('piecework_PU', models.PositiveSmallIntegerField(verbose_name='Сдельная станок ПУ')),
                ('piecework_EVA', models.PositiveSmallIntegerField(verbose_name='Сдельная ЕВА')),
                ('accrued', models.PositiveSmallIntegerField(verbose_name='Начислено')),
                ('premium', models.PositiveSmallIntegerField(verbose_name='Премия')),
                ('avans', models.PositiveSmallIntegerField(verbose_name='Аванс')),
                ('sale_goods', models.PositiveSmallIntegerField(verbose_name='Продажа товаров')),
                ('pay', models.PositiveSmallIntegerField(verbose_name='Выплата')),
                ('rest', models.PositiveSmallIntegerField(verbose_name='Остаток')),
                ('date', models.DateField(verbose_name='Дата')),
                ('tabel_employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.worker', verbose_name='ФИО')),
            ],
            options={
                'verbose_name': 'Общая зарплата',
                'verbose_name_plural': 'Общие зарплаты',
            },
        ),
    ]