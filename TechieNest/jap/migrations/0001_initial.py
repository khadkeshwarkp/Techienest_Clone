# Generated by Django 2.0.5 on 2018-11-25 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingRegistrationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('contact_no', models.CharField(max_length=10)),
                ('hometown', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('-- select state --', '-- select state --'), ('Andaman & Nicobar Island', 'Andaman & Nicobar Island'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andra Pradesh', 'Andra Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chattisgarh', 'Chattisgarh'), ('Delhi', 'Delhi'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman & Diu', 'Daman & Diu'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerela', 'Kerela'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Punjab', 'Pondicherry'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Tripura', 'Tripura'), ('Telangana', 'Telangana'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('Uttaranchal', 'Uttaranchal'), ('West Bengal', 'West Bengal')], default='-- select state --', max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('current_semester', models.CharField(choices=[('-- current semester --', '-- current semester --'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('Passout', 'Passout')], default='-- current semester --', max_length=50)),
                ('registration_for', models.CharField(choices=[('-- select registration for --', '-- select registration for --'), ('Summer industrial internship/training program', 'Summer industrial internship/training program'), ('Winter industrial internship/training program', 'Winter industrial internship/training program'), ('Regular training program', 'Regular training program'), ('Weekend training program', 'Weekend training program'), ('Job assurance program', 'Job assurance program')], default='-- select registration for --', max_length=100)),
                ('previous_exp', models.CharField(choices=[('-- select --', '-- select --'), ('SITP', 'SITP'), ('WITP', 'WITP'), ('Workshop', 'Workshop'), ('Internship', 'Internship'), ('Others', 'Others')], default='-- select --', max_length=200)),
                ('how_did_you_know', models.CharField(max_length=200)),
                ('techienest_contactperson', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
