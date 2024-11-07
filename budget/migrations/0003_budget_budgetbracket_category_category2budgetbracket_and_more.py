# Generated by Django 4.2.16 on 2024-10-24 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_alter_account_id_acccountentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BudgetBracket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('budget_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budget', to='budget.budget')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_file', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.CharField(max_length=120)),
                ('is_expense', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category2BudgetBracket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('budget_bracket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budget_bracket', to='budget.budgetbracket')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budget_bracket_category', to='budget.category')),
            ],
        ),
        migrations.AddField(
            model_name='acccountentry',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='account_name_category', to='budget.category'),
            preserve_default=False,
        ),
    ]