# Generated by Django 3.0.4 on 2020-04-24 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyt', '0002_auto_20200424_1950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amc',
            options={'verbose_name_plural': 'AMC'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Customer'},
        ),
        migrations.AlterModelOptions(
            name='employee_details',
            options={'verbose_name_plural': 'Employee_Details'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name_plural': 'Purchase'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name_plural': 'Shop'},
        ),
        migrations.AlterModelOptions(
            name='supplier_detail',
            options={'verbose_name_plural': 'Supplier_detail'},
        ),
        migrations.AlterModelOptions(
            name='supplies',
            options={'verbose_name_plural': 'Supplies'},
        ),
        migrations.AlterModelTable(
            name='amc',
            table='AMC',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='Customer',
        ),
        migrations.AlterModelTable(
            name='employee_details',
            table='Employee_Details',
        ),
        migrations.AlterModelTable(
            name='purchase',
            table='Purchase',
        ),
        migrations.AlterModelTable(
            name='shop',
            table='Shop',
        ),
        migrations.AlterModelTable(
            name='supplier_detail',
            table='Supplier_detail',
        ),
        migrations.AlterModelTable(
            name='supplies',
            table='Supplies',
        ),
    ]
