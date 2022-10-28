# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-03 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icf_career_fair', '0012_auto_20211001_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerfairandproductoptional',
            name='career_fair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career_fair_draft_products', to='icf_career_fair.CareerFairDraft'),
        ),
        migrations.AlterField(
            model_name='careerfairandproductoptional',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career_fair_draft_products', to='icf_orders.ProductDraft'),
        ),
    ]