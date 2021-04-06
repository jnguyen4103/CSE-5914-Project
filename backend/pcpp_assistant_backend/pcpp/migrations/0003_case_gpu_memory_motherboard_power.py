# Generated by Django 3.1.7 on 2021-04-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcpp', '0002_auto_20210401_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.TextField()),
                ('minPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Color', models.TextField()),
                ('Dimensions', models.TextField()),
                ('External_Bays', models.IntegerField()),
                ('Front_Panel_USB', models.TextField()),
                ('Full_Height_Expansion_Slots', models.IntegerField()),
                ('Half_Height_Expansion_Slots', models.IntegerField()),
                ('Internal_Twoin_Bays', models.IntegerField()),
                ('Internal_Threein_Bays', models.IntegerField()),
                ('Manufacturer', models.TextField()),
                ('Maximum_Video_Card_Length', models.TextField()),
                ('Model', models.TextField()),
                ('Motherboard_Form_Factor', models.TextField()),
                ('Part_num', models.TextField()),
                ('Power_Supply', models.TextField()),
                ('Power_Supply_Shroud', models.TextField()),
                ('Side_Panel_Window', models.TextField()),
                ('Type', models.TextField()),
                ('Volume', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.TextField()),
                ('minPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Boost_Clock', models.FloatField()),
                ('Chipset', models.TextField()),
                ('Color', models.TextField()),
                ('Cooling', models.TextField()),
                ('Core_Clock', models.FloatField()),
                ('Dvi_Ports', models.IntegerField()),
                ('DVI_D_Dual_Link', models.IntegerField()),
                ('DisplayPort', models.IntegerField()),
                ('DisplayPort_Ports', models.IntegerField()),
                ('Effective_Memory_Clock', models.FloatField()),
                ('Expansion_Slot_Width', models.TextField()),
                ('External_Power', models.TextField()),
                ('Frame_Sync', models.TextField()),
                ('HDMI_Ports', models.TextField()),
                ('Interface', models.TextField()),
                ('Length', models.TextField()),
                ('Manufacturer', models.TextField()),
                ('Memory', models.IntegerField()),
                ('Memory_Type', models.TextField()),
                ('Mini_DisplayPort_Ports', models.TextField()),
                ('Mini_HDMI_Ports', models.TextField()),
                ('Part_num', models.TextField()),
                ('TDP', models.IntegerField()),
                ('VGA', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.TextField()),
                ('minPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CAS_Latency', models.IntegerField()),
                ('Color', models.TextField()),
                ('ECC_Registered', models.TextField()),
                ('First_Word_Latency', models.FloatField()),
                ('Form_Factor', models.TextField()),
                ('Heat_Spreader', models.TextField()),
                ('Manufacturer', models.TextField()),
                ('Modules', models.TextField()),
                ('Part_num', models.TextField()),
                ('Price_GB', models.TextField()),
                ('Voltage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.TextField()),
                ('minPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Chipset', models.TextField()),
                ('Color', models.TextField()),
                ('Form_Factor', models.TextField()),
                ('Manufacturer', models.TextField()),
                ('Memory_Max', models.IntegerField()),
                ('Memory_Slots', models.IntegerField()),
                ('Memory_Speed', models.TextField()),
                ('Memory_Type', models.TextField()),
                ('Model', models.TextField()),
                ('Onboard_Ethernet', models.TextField()),
                ('Onboard_Video', models.TextField()),
                ('PCI_Slots', models.IntegerField()),
                ('PCI_E_one_Slots', models.IntegerField()),
                ('PCI_E_sixteen_Slots', models.IntegerField()),
                ('PCI_E_four_Slots', models.IntegerField()),
                ('PCI_E_eight_Slots', models.IntegerField()),
                ('Part_num', models.TextField()),
                ('RAID_Support', models.TextField()),
                ('SATA_three_Gbs', models.IntegerField()),
                ('SATA_six_Gbs', models.IntegerField()),
                ('Socket_CPU', models.TextField()),
                ('Supports_ECC', models.TextField()),
                ('USB_two_Headers', models.IntegerField()),
                ('USB_three_Gen_one_Headers', models.IntegerField()),
                ('USB_three_Gen_two_Headers', models.IntegerField()),
                ('USB_three_Gen_twoxtwo_Headers', models.IntegerField()),
                ('Wireless_Networking', models.TextField()),
                ('eSATA_threeGbs', models.IntegerField()),
                ('mSATA_Slots', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.TextField()),
                ('minPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Color', models.TextField()),
                ('EPS_Connectors', models.IntegerField()),
                ('Efficiency', models.TextField()),
                ('Efficiency_Rating', models.TextField()),
                ('Fanless', models.TextField()),
                ('Form_Factor', models.TextField()),
                ('Length', models.TextField()),
                ('Manufacturer', models.TextField()),
                ('Modular', models.TextField()),
                ('Molex_fourPin_Connectors', models.IntegerField()),
                ('Output', models.TextField()),
                ('PCIe_sixtwoPin_Connectors', models.IntegerField()),
                ('Part_num', models.TextField()),
                ('SATA_Connectors', models.IntegerField()),
                ('Type', models.TextField()),
                ('Wattage', models.IntegerField()),
            ],
        ),
    ]
