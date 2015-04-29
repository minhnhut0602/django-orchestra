# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billcontact',
            name='country',
            field=models.CharField(choices=[('EE', 'Estonia'), ('PH', 'Philippines'), ('BT', 'Bhutan'), ('LA', "Lao People's Democratic Republic"), ('DJ', 'Djibouti'), ('TK', 'Tokelau'), ('IM', 'Isle of Man'), ('SR', 'Suriname'), ('KP', "Korea (the Democratic People's Republic of)"), ('JP', 'Japan'), ('KN', 'Saint Kitts and Nevis'), ('SY', 'Syrian Arab Republic'), ('AG', 'Antigua and Barbuda'), ('RW', 'Rwanda'), ('PA', 'Panama'), ('CA', 'Canada'), ('MR', 'Mauritania'), ('HK', 'Hong Kong'), ('UM', 'United States Minor Outlying Islands'), ('BB', 'Barbados'), ('NF', 'Norfolk Island'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('GS', 'South Georgia and the South Sandwich Islands'), ('FK', 'Falkland Islands  [Malvinas]'), ('TF', 'French Southern Territories'), ('TV', 'Tuvalu'), ('SX', 'Sint Maarten (Dutch part)'), ('PW', 'Palau'), ('QA', 'Qatar'), ('GT', 'Guatemala'), ('KG', 'Kyrgyzstan'), ('HT', 'Haiti'), ('NG', 'Nigeria'), ('TG', 'Togo'), ('GR', 'Greece'), ('GF', 'French Guiana'), ('HN', 'Honduras'), ('CV', 'Cabo Verde'), ('DM', 'Dominica'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('ME', 'Montenegro'), ('SG', 'Singapore'), ('MT', 'Malta'), ('GG', 'Guernsey'), ('MW', 'Malawi'), ('GH', 'Ghana'), ('GN', 'Guinea'), ('EG', 'Egypt'), ('MD', 'Moldova (the Republic of)'), ('NE', 'Niger'), ('NR', 'Nauru'), ('IE', 'Ireland'), ('CY', 'Cyprus'), ('BH', 'Bahrain'), ('BY', 'Belarus'), ('TC', 'Turks and Caicos Islands'), ('CF', 'Central African Republic'), ('CI', "Côte d'Ivoire"), ('LK', 'Sri Lanka'), ('GW', 'Guinea-Bissau'), ('SZ', 'Swaziland'), ('YE', 'Yemen'), ('AQ', 'Antarctica'), ('WS', 'Samoa'), ('PN', 'Pitcairn'), ('AE', 'United Arab Emirates'), ('LV', 'Latvia'), ('CZ', 'Czech Republic'), ('JO', 'Jordan'), ('LU', 'Luxembourg'), ('RU', 'Russian Federation'), ('SN', 'Senegal'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SS', 'South Sudan'), ('LI', 'Liechtenstein'), ('GM', 'Gambia'), ('SO', 'Somalia'), ('AT', 'Austria'), ('AL', 'Albania'), ('MM', 'Myanmar'), ('MC', 'Monaco'), ('AZ', 'Azerbaijan'), ('KY', 'Cayman Islands'), ('HU', 'Hungary'), ('SE', 'Sweden'), ('US', 'United States of America'), ('MS', 'Montserrat'), ('MX', 'Mexico'), ('IR', 'Iran (Islamic Republic of)'), ('SK', 'Slovakia'), ('IO', 'British Indian Ocean Territory'), ('SV', 'El Salvador'), ('ST', 'Sao Tome and Principe'), ('ZW', 'Zimbabwe'), ('MN', 'Mongolia'), ('MG', 'Madagascar'), ('LB', 'Lebanon'), ('PR', 'Puerto Rico'), ('JE', 'Jersey'), ('BD', 'Bangladesh'), ('HM', 'Heard Island and McDonald Islands'), ('RO', 'Romania'), ('TN', 'Tunisia'), ('AD', 'Andorra'), ('SJ', 'Svalbard and Jan Mayen'), ('PL', 'Poland'), ('AF', 'Afghanistan'), ('NC', 'New Caledonia'), ('FI', 'Finland'), ('GD', 'Grenada'), ('GY', 'Guyana'), ('ZA', 'South Africa'), ('MA', 'Morocco'), ('AS', 'American Samoa'), ('PY', 'Paraguay'), ('ZM', 'Zambia'), ('PG', 'Papua New Guinea'), ('CH', 'Switzerland'), ('LY', 'Libya'), ('KZ', 'Kazakhstan'), ('SL', 'Sierra Leone'), ('DO', 'Dominican Republic'), ('TZ', 'Tanzania, United Republic of'), ('LC', 'Saint Lucia'), ('NI', 'Nicaragua'), ('TH', 'Thailand'), ('BI', 'Burundi'), ('SD', 'Sudan'), ('BW', 'Botswana'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('TJ', 'Tajikistan'), ('CM', 'Cameroon'), ('EC', 'Ecuador'), ('ER', 'Eritrea'), ('CX', 'Christmas Island'), ('MO', 'Macao'), ('MH', 'Marshall Islands'), ('AU', 'Australia'), ('DK', 'Denmark'), ('TT', 'Trinidad and Tobago'), ('BE', 'Belgium'), ('SI', 'Slovenia'), ('PM', 'Saint Pierre and Miquelon'), ('KH', 'Cambodia'), ('CW', 'Curaçao'), ('EH', 'Western Sahara'), ('TO', 'Tonga'), ('AO', 'Angola'), ('OM', 'Oman'), ('GE', 'Georgia'), ('MF', 'Saint Martin (French part)'), ('IT', 'Italy'), ('UA', 'Ukraine'), ('BA', 'Bosnia and Herzegovina'), ('WF', 'Wallis and Futuna'), ('FM', 'Micronesia (Federated States of)'), ('BO', 'Bolivia (Plurinational State of)'), ('PF', 'French Polynesia'), ('DE', 'Germany'), ('BZ', 'Belize'), ('IS', 'Iceland'), ('MY', 'Malaysia'), ('IQ', 'Iraq'), ('KR', 'Korea (the Republic of)'), ('CN', 'China'), ('SB', 'Solomon Islands'), ('TL', 'Timor-Leste'), ('TD', 'Chad'), ('PE', 'Peru'), ('BL', 'Saint Barthélemy'), ('CL', 'Chile'), ('KI', 'Kiribati'), ('PT', 'Portugal'), ('ES', 'Spain'), ('IL', 'Israel'), ('MU', 'Mauritius'), ('HR', 'Croatia'), ('PK', 'Pakistan'), ('PS', 'Palestine, State of'), ('NL', 'Netherlands'), ('CG', 'Congo'), ('MQ', 'Martinique'), ('BG', 'Bulgaria'), ('FR', 'France'), ('VI', 'Virgin Islands (U.S.)'), ('LT', 'Lithuania'), ('BN', 'Brunei Darussalam'), ('ET', 'Ethiopia'), ('NU', 'Niue'), ('AR', 'Argentina'), ('DZ', 'Algeria'), ('RS', 'Serbia'), ('UZ', 'Uzbekistan'), ('SM', 'San Marino'), ('JM', 'Jamaica'), ('VN', 'Viet Nam'), ('AM', 'Armenia'), ('KE', 'Kenya'), ('CO', 'Colombia'), ('LS', 'Lesotho'), ('GP', 'Guadeloupe'), ('GA', 'Gabon'), ('KM', 'Comoros'), ('BS', 'Bahamas'), ('TW', 'Taiwan (Province of China)'), ('RE', 'Réunion'), ('AW', 'Aruba'), ('BV', 'Bouvet Island'), ('UG', 'Uganda'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BF', 'Burkina Faso'), ('NP', 'Nepal'), ('VG', 'Virgin Islands (British)'), ('SA', 'Saudi Arabia'), ('AX', 'Åland Islands'), ('TM', 'Turkmenistan'), ('IN', 'India'), ('CC', 'Cocos (Keeling) Islands'), ('FO', 'Faroe Islands'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('ID', 'Indonesia'), ('NA', 'Namibia'), ('TR', 'Turkey'), ('GI', 'Gibraltar'), ('GQ', 'Equatorial Guinea'), ('GU', 'Guam'), ('ML', 'Mali'), ('SC', 'Seychelles'), ('MP', 'Northern Mariana Islands'), ('LR', 'Liberia'), ('CK', 'Cook Islands'), ('VA', 'Holy See'), ('FJ', 'Fiji'), ('YT', 'Mayotte'), ('NZ', 'New Zealand'), ('CU', 'Cuba'), ('AI', 'Anguilla'), ('VC', 'Saint Vincent and the Grenadines'), ('MV', 'Maldives'), ('GL', 'Greenland'), ('NO', 'Norway'), ('BR', 'Brazil'), ('CD', 'Congo (the Democratic Republic of the)'), ('CR', 'Costa Rica'), ('VU', 'Vanuatu'), ('MZ', 'Mozambique'), ('KW', 'Kuwait'), ('UY', 'Uruguay')], verbose_name='country', max_length=20, default='ES'),
        ),
    ]
