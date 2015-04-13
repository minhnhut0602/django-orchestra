# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.CharField(max_length=20, verbose_name='country', default='ES', blank=True, choices=[('EE', 'Estonia'), ('AI', 'Anguilla'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('LB', 'Lebanon'), ('MO', 'Macao'), ('PF', 'French Polynesia'), ('CI', "Côte d'Ivoire"), ('VC', 'Saint Vincent and the Grenadines'), ('PR', 'Puerto Rico'), ('PW', 'Palau'), ('PA', 'Panama'), ('TL', 'Timor-Leste'), ('SD', 'Sudan'), ('TT', 'Trinidad and Tobago'), ('CA', 'Canada'), ('MS', 'Montserrat'), ('DE', 'Germany'), ('HR', 'Croatia'), ('KN', 'Saint Kitts and Nevis'), ('SC', 'Seychelles'), ('TC', 'Turks and Caicos Islands'), ('AR', 'Argentina'), ('VN', 'Viet Nam'), ('NO', 'Norway'), ('MY', 'Malaysia'), ('IO', 'British Indian Ocean Territory'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('PL', 'Poland'), ('BW', 'Botswana'), ('CZ', 'Czech Republic'), ('AG', 'Antigua and Barbuda'), ('TR', 'Turkey'), ('NC', 'New Caledonia'), ('ZM', 'Zambia'), ('MV', 'Maldives'), ('BO', 'Bolivia (Plurinational State of)'), ('CM', 'Cameroon'), ('BZ', 'Belize'), ('SO', 'Somalia'), ('AE', 'United Arab Emirates'), ('YE', 'Yemen'), ('UY', 'Uruguay'), ('GG', 'Guernsey'), ('QA', 'Qatar'), ('IN', 'India'), ('FJ', 'Fiji'), ('MZ', 'Mozambique'), ('CO', 'Colombia'), ('EC', 'Ecuador'), ('SK', 'Slovakia'), ('UM', 'United States Minor Outlying Islands'), ('CR', 'Costa Rica'), ('TV', 'Tuvalu'), ('AZ', 'Azerbaijan'), ('IE', 'Ireland'), ('EG', 'Egypt'), ('GL', 'Greenland'), ('US', 'United States of America'), ('BT', 'Bhutan'), ('ZA', 'South Africa'), ('NP', 'Nepal'), ('TO', 'Tonga'), ('TJ', 'Tajikistan'), ('VG', 'Virgin Islands (British)'), ('RE', 'Réunion'), ('NR', 'Nauru'), ('DK', 'Denmark'), ('LT', 'Lithuania'), ('ET', 'Ethiopia'), ('TZ', 'Tanzania, United Republic of'), ('SB', 'Solomon Islands'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('SG', 'Singapore'), ('MF', 'Saint Martin (French part)'), ('FI', 'Finland'), ('LK', 'Sri Lanka'), ('NU', 'Niue'), ('TM', 'Turkmenistan'), ('SJ', 'Svalbard and Jan Mayen'), ('GN', 'Guinea'), ('BB', 'Barbados'), ('VU', 'Vanuatu'), ('AL', 'Albania'), ('JM', 'Jamaica'), ('ID', 'Indonesia'), ('CL', 'Chile'), ('IT', 'Italy'), ('PT', 'Portugal'), ('KP', "Korea (the Democratic People's Republic of)"), ('MU', 'Mauritius'), ('PY', 'Paraguay'), ('MH', 'Marshall Islands'), ('TH', 'Thailand'), ('IQ', 'Iraq'), ('LR', 'Liberia'), ('NA', 'Namibia'), ('NL', 'Netherlands'), ('AX', 'Åland Islands'), ('MX', 'Mexico'), ('KW', 'Kuwait'), ('ZW', 'Zimbabwe'), ('GQ', 'Equatorial Guinea'), ('UA', 'Ukraine'), ('OM', 'Oman'), ('TD', 'Chad'), ('SR', 'Suriname'), ('KM', 'Comoros'), ('CF', 'Central African Republic'), ('GP', 'Guadeloupe'), ('LU', 'Luxembourg'), ('LC', 'Saint Lucia'), ('SY', 'Syrian Arab Republic'), ('HU', 'Hungary'), ('VA', 'Holy See'), ('KY', 'Cayman Islands'), ('CN', 'China'), ('KR', 'Korea (the Republic of)'), ('DZ', 'Algeria'), ('GE', 'Georgia'), ('CY', 'Cyprus'), ('LA', "Lao People's Democratic Republic"), ('GH', 'Ghana'), ('AT', 'Austria'), ('DO', 'Dominican Republic'), ('MN', 'Mongolia'), ('SI', 'Slovenia'), ('NG', 'Nigeria'), ('GM', 'Gambia'), ('AF', 'Afghanistan'), ('NE', 'Niger'), ('AO', 'Angola'), ('MW', 'Malawi'), ('PN', 'Pitcairn'), ('NZ', 'New Zealand'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('RW', 'Rwanda'), ('AU', 'Australia'), ('CK', 'Cook Islands'), ('BJ', 'Benin'), ('SS', 'South Sudan'), ('GU', 'Guam'), ('LI', 'Liechtenstein'), ('MR', 'Mauritania'), ('FM', 'Micronesia (Federated States of)'), ('BY', 'Belarus'), ('PH', 'Philippines'), ('ER', 'Eritrea'), ('RU', 'Russian Federation'), ('YT', 'Mayotte'), ('BI', 'Burundi'), ('AS', 'American Samoa'), ('MA', 'Morocco'), ('BD', 'Bangladesh'), ('TN', 'Tunisia'), ('NI', 'Nicaragua'), ('HT', 'Haiti'), ('AQ', 'Antarctica'), ('BR', 'Brazil'), ('FK', 'Falkland Islands  [Malvinas]'), ('AM', 'Armenia'), ('MG', 'Madagascar'), ('MC', 'Monaco'), ('IM', 'Isle of Man'), ('KI', 'Kiribati'), ('FO', 'Faroe Islands'), ('SZ', 'Swaziland'), ('GR', 'Greece'), ('PS', 'Palestine, State of'), ('GY', 'Guyana'), ('MQ', 'Martinique'), ('ML', 'Mali'), ('BM', 'Bermuda'), ('CU', 'Cuba'), ('MD', 'Moldova (the Republic of)'), ('CX', 'Christmas Island'), ('TF', 'French Southern Territories'), ('KE', 'Kenya'), ('CH', 'Switzerland'), ('SM', 'San Marino'), ('TK', 'Tokelau'), ('EH', 'Western Sahara'), ('IS', 'Iceland'), ('DM', 'Dominica'), ('SE', 'Sweden'), ('NF', 'Norfolk Island'), ('MM', 'Myanmar'), ('CD', 'Congo (the Democratic Republic of the)'), ('JP', 'Japan'), ('BS', 'Bahamas'), ('ES', 'Spain'), ('GI', 'Gibraltar'), ('AD', 'Andorra'), ('RO', 'Romania'), ('CV', 'Cabo Verde'), ('HN', 'Honduras'), ('GT', 'Guatemala'), ('KG', 'Kyrgyzstan'), ('WS', 'Samoa'), ('PG', 'Papua New Guinea'), ('VI', 'Virgin Islands (U.S.)'), ('BG', 'Bulgaria'), ('RS', 'Serbia'), ('LS', 'Lesotho'), ('GA', 'Gabon'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('BN', 'Brunei Darussalam'), ('CC', 'Cocos (Keeling) Islands'), ('SN', 'Senegal'), ('BE', 'Belgium'), ('BA', 'Bosnia and Herzegovina'), ('HK', 'Hong Kong'), ('DJ', 'Djibouti'), ('GF', 'French Guiana'), ('UZ', 'Uzbekistan'), ('HM', 'Heard Island and McDonald Islands'), ('IL', 'Israel'), ('MP', 'Northern Mariana Islands'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('SX', 'Sint Maarten (Dutch part)'), ('CG', 'Congo'), ('SV', 'El Salvador'), ('AW', 'Aruba'), ('BL', 'Saint Barthélemy'), ('MT', 'Malta'), ('LV', 'Latvia'), ('UG', 'Uganda'), ('PE', 'Peru'), ('KZ', 'Kazakhstan'), ('PK', 'Pakistan'), ('TG', 'Togo'), ('WF', 'Wallis and Futuna'), ('GS', 'South Georgia and the South Sandwich Islands'), ('GD', 'Grenada'), ('PM', 'Saint Pierre and Miquelon'), ('BV', 'Bouvet Island'), ('KH', 'Cambodia'), ('BH', 'Bahrain'), ('GW', 'Guinea-Bissau'), ('ME', 'Montenegro'), ('SL', 'Sierra Leone'), ('IR', 'Iran (Islamic Republic of)'), ('JO', 'Jordan'), ('BF', 'Burkina Faso'), ('LY', 'Libya'), ('FR', 'France'), ('TW', 'Taiwan (Province of China)'), ('CW', 'Curaçao'), ('JE', 'Jersey')]),
        ),
    ]