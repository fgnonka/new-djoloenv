"""List of all languages supported in Djolowin.

Generated with Babel:

from babel import Locale
from babel.localedata import locale_identifiers

EXCLUDE = [
    "ar_001",
    "en_US_POSIX",
    "en_001",
    "en_150",
    "eo_001",
    "es_419",
    "ia_001",
    "prg_001",
    "vo_001",
    "yi_001",
]

languages = []

for lid in sorted(locale_identifiers()):
    if lid not in EXCLUDE:
        languages.append((lid.replace("_", "-"), Locale.parse(lid).english_name))
"""


LANGUAGES = [
    ("af", "Afrikaans"),
    ("af-na", "Afrikaans (Namibia)"),
    ("af-za", "Afrikaans (South Africa)"),
    ("agq", "Aghem"),
    ("agq-cm", "Aghem (Cameroon)"),
    ("ak", "Akan"),
    ("ak-gh", "Akan (Ghana)"),
    ("am", "Amharic"),
    ("am-et", "Amharic (Ethiopia)"),
    ("ar", "Arabic"),
    ("ar-ae", "Arabic (United Arab Emirates)"),
    ("ar-bh", "Arabic (Bahrain)"),
    ("ar-dj", "Arabic (Djibouti)"),
    ("ar-dz", "Arabic (Algeria)"),
    ("ar-eg", "Arabic (Egypt)"),
    ("ar-eh", "Arabic (Western Sahara)"),
    ("ar-er", "Arabic (Eritrea)"),
    ("ar-il", "Arabic (Israel)"),
    ("ar-iq", "Arabic (Iraq)"),
    ("ar-jo", "Arabic (Jordan)"),
    ("ar-km", "Arabic (Comoros)"),
    ("ar-kw", "Arabic (Kuwait)"),
    ("ar-lb", "Arabic (Lebanon)"),
    ("ar-ly", "Arabic (Libya)"),
    ("ar-ma", "Arabic (Morocco)"),
    ("ar-mr", "Arabic (Mauritania)"),
    ("ar-om", "Arabic (Oman)"),
    ("ar-ps", "Arabic (Palestinian Territories)"),
    ("ar-qa", "Arabic (Qatar)"),
    ("ar-sa", "Arabic (Saudi Arabia)"),
    ("ar-sd", "Arabic (Sudan)"),
    ("ar-so", "Arabic (Somalia)"),
    ("ar-ss", "Arabic (South Sudan)"),
    ("ar-sy", "Arabic (Syria)"),
    ("ar-td", "Arabic (Chad)"),
    ("ar-tn", "Arabic (Tunisia)"),
    ("ar-ye", "Arabic (Yemen)"),
    ("as", "Assamese"),
    ("as-in", "Assamese (India)"),
    ("asa", "Asu"),
    ("asa-tz", "Asu (Tanzania)"),
    ("ast", "Asturian"),
    ("ast-es", "Asturian (Spain)"),
    ("az", "Azerbaijani"),
    ("az-cyrl", "Azerbaijani (Cyrillic)"),
    ("az-cyrl-az", "Azerbaijani (Cyrillic, Azerbaijan)"),
    ("az-latn", "Azerbaijani (Latin)"),
    ("az-latn-az", "Azerbaijani (Latin, Azerbaijan)"),
    ("bas", "Basaa"),
    ("bas-cm", "Basaa (Cameroon)"),
    ("be", "Belarusian"),
    ("be-by", "Belarusian (Belarus)"),
    ("bem", "Bemba"),
    ("bem-zm", "Bemba (Zambia)"),
    ("bez", "Bena"),
    ("bez-tz", "Bena (Tanzania)"),
    ("bg", "Bulgarian"),
    ("bg-bg", "Bulgarian (Bulgaria)"),
    ("bm", "Bambara"),
    ("bm-ml", "Bambara (Mali)"),
    ("bn", "Bangla"),
    ("bn-bd", "Bangla (Bangladesh)"),
    ("bn-in", "Bangla (India)"),
    ("bo", "Tibetan"),
    ("bo-cn", "Tibetan (China)"),
    ("bo-in", "Tibetan (India)"),
    ("br", "Breton"),
    ("br-fr", "Breton (France)"),
    ("brx", "Bodo"),
    ("brx-in", "Bodo (India)"),
    ("bs", "Bosnian"),
    ("bs-cyrl", "Bosnian (Cyrillic)"),
    ("bs-cyrl-ba", "Bosnian (Cyrillic, Bosnia & Herzegovina)"),
    ("bs-latn", "Bosnian (Latin)"),
    ("bs-latn-ba", "Bosnian (Latin, Bosnia & Herzegovina)"),
    ("ca", "Catalan"),
    ("ca-ad", "Catalan (Andorra)"),
    ("ca-es", "Catalan (Spain)"),
    ("ca-es-valencia", "Catalan (Spain, Valencian)"),
    ("ca-fr", "Catalan (France)"),
    ("ca-it", "Catalan (Italy)"),
    ("ccp", "Chakma"),
    ("ccp-bd", "Chakma (Bangladesh)"),
    ("ccp-in", "Chakma (India)"),
    ("ce", "Chechen"),
    ("ce-ru", "Chechen (Russia)"),
    ("ceb", "Cebuano"),
    ("ceb-ph", "Cebuano (Philippines)"),
    ("cgg", "Chiga"),
    ("cgg-ug", "Chiga (Uganda)"),
    ("chr", "Cherokee"),
    ("chr-us", "Cherokee (United States)"),
    ("ckb", "Central Kurdish"),
    ("ckb-iq", "Central Kurdish (Iraq)"),
    ("ckb-ir", "Central Kurdish (Iran)"),
    ("cs", "Czech"),
    ("cs-cz", "Czech (Czechia)"),
    ("cu", "Church Slavic"),
    ("cu-ru", "Church Slavic (Russia)"),
    ("cy", "Welsh"),
    ("cy-gb", "Welsh (United Kingdom)"),
    ("da", "Danish"),
    ("da-dk", "Danish (Denmark)"),
    ("da-gl", "Danish (Greenland)"),
    ("dav", "Taita"),
    ("dav-ke", "Taita (Kenya)"),
    ("de", "German"),
    ("de-at", "German (Austria)"),
    ("de-be", "German (Belgium)"),
    ("de-ch", "German (Switzerland)"),
    ("de-de", "German (Germany)"),
    ("de-it", "German (Italy)"),
    ("de-li", "German (Liechtenstein)"),
    ("de-lu", "German (Luxembourg)"),
    ("dje", "Zarma"),
    ("dje-ne", "Zarma (Niger)"),
    ("dsb", "Lower Sorbian"),
    ("dsb-de", "Lower Sorbian (Germany)"),
    ("dua", "Duala"),
    ("dua-cm", "Duala (Cameroon)"),
    ("dyo", "Jola-Fonyi"),
    ("dyo-sn", "Jola-Fonyi (Senegal)"),
    ("dz", "Dzongkha"),
    ("dz-bt", "Dzongkha (Bhutan)"),
    ("ebu", "Embu"),
    ("ebu-ke", "Embu (Kenya)"),
    ("ee", "Ewe"),
    ("ee-gh", "Ewe (Ghana)"),
    ("ee-tg", "Ewe (Togo)"),
    ("el", "Greek"),
    ("el-cy", "Greek (Cyprus)"),
    ("el-gr", "Greek (Greece)"),
    ("en", "English"),
    ("en-ae", "English (United Arab Emirates)"),
    ("en-ag", "English (Antigua & Barbuda)"),
    ("en-ai", "English (Anguilla)"),
    ("en-as", "English (American Samoa)"),
    ("en-at", "English (Austria)"),
    ("en-au", "English (Australia)"),
    ("en-bb", "English (Barbados)"),
    ("en-be", "English (Belgium)"),
    ("en-bi", "English (Burundi)"),
    ("en-bm", "English (Bermuda)"),
    ("en-bs", "English (Bahamas)"),
    ("en-bw", "English (Botswana)"),
    ("en-bz", "English (Belize)"),
    ("en-ca", "English (Canada)"),
    ("en-cc", "English (Cocos (Keeling) Islands)"),
    ("en-ch", "English (Switzerland)"),
    ("en-ck", "English (Cook Islands)"),
    ("en-cm", "English (Cameroon)"),
    ("en-cx", "English (Christmas Island)"),
    ("en-cy", "English (Cyprus)"),
    ("en-de", "English (Germany)"),
    ("en-dg", "English (Diego Garcia)"),
    ("en-dk", "English (Denmark)"),
    ("en-dm", "English (Dominica)"),
    ("en-er", "English (Eritrea)"),
    ("en-fi", "English (Finland)"),
    ("en-fj", "English (Fiji)"),
    ("en-fk", "English (Falkland Islands)"),
    ("en-fm", "English (Micronesia)"),
    ("en-gb", "English (United Kingdom)"),
    ("en-gd", "English (Grenada)"),
    ("en-gg", "English (Guernsey)"),
    ("en-gh", "English (Ghana)"),
    ("en-gi", "English (Gibraltar)"),
    ("en-gm", "English (Gambia)"),
    ("en-gu", "English (Guam)"),
    ("en-gy", "English (Guyana)"),
    ("en-hk", "English (Hong Kong SAR China)"),
    ("en-ie", "English (Ireland)"),
    ("en-il", "English (Israel)"),
    ("en-im", "English (Isle of Man)"),
    ("en-in", "English (India)"),
    ("en-io", "English (British Indian Ocean Territory)"),
    ("en-je", "English (Jersey)"),
    ("en-jm", "English (Jamaica)"),
    ("en-ke", "English (Kenya)"),
    ("en-ki", "English (Kiribati)"),
    ("en-kn", "English (St. Kitts & Nevis)"),
    ("en-ky", "English (Cayman Islands)"),
    ("en-lc", "English (St. Lucia)"),
    ("en-lr", "English (Liberia)"),
    ("en-ls", "English (Lesotho)"),
    ("en-mg", "English (Madagascar)"),
    ("en-mh", "English (Marshall Islands)"),
    ("en-mo", "English (Macao SAR China)"),
    ("en-mp", "English (Northern Mariana Islands)"),
    ("en-ms", "English (Montserrat)"),
    ("en-mt", "English (Malta)"),
    ("en-mu", "English (Mauritius)"),
    ("en-mw", "English (Malawi)"),
    ("en-my", "English (Malaysia)"),
    ("en-na", "English (Namibia)"),
    ("en-nf", "English (Norfolk Island)"),
    ("en-ng", "English (Nigeria)"),
    ("en-nl", "English (Netherlands)"),
    ("en-nr", "English (Nauru)"),
    ("en-nu", "English (Niue)"),
    ("en-nz", "English (New Zealand)"),
    ("en-pg", "English (Papua New Guinea)"),
    ("en-ph", "English (Philippines)"),
    ("en-pk", "English (Pakistan)"),
    ("en-pn", "English (Pitcairn Islands)"),
    ("en-pr", "English (Puerto Rico)"),
    ("en-pw", "English (Palau)"),
    ("en-rw", "English (Rwanda)"),
    ("en-sb", "English (Solomon Islands)"),
    ("en-sc", "English (Seychelles)"),
    ("en-sd", "English (Sudan)"),
    ("en-se", "English (Sweden)"),
    ("en-sg", "English (Singapore)"),
    ("en-sh", "English (St. Helena)"),
    ("en-si", "English (Slovenia)"),
    ("en-sl", "English (Sierra Leone)"),
    ("en-ss", "English (South Sudan)"),
    ("en-sx", "English (Sint Maarten)"),
    ("en-sz", "English (Eswatini)"),
    ("en-tc", "English (Turks & Caicos Islands)"),
    ("en-tk", "English (Tokelau)"),
    ("en-to", "English (Tonga)"),
    ("en-tt", "English (Trinidad & Tobago)"),
    ("en-tv", "English (Tuvalu)"),
    ("en-tz", "English (Tanzania)"),
    ("en-ug", "English (Uganda)"),
    ("en-um", "English (U.S. Outlying Islands)"),
    ("en-us", "English (United States)"),
    ("en-vc", "English (St. Vincent & Grenadines)"),
    ("en-vg", "English (British Virgin Islands)"),
    ("en-vi", "English (U.S. Virgin Islands)"),
    ("en-vu", "English (Vanuatu)"),
    ("en-ws", "English (Samoa)"),
    ("en-za", "English (South Africa)"),
    ("en-zm", "English (Zambia)"),
    ("en-zw", "English (Zimbabwe)"),
    ("eo", "Esperanto"),
    ("es", "Spanish"),
    ("es-ar", "Spanish (Argentina)"),
    ("es-bo", "Spanish (Bolivia)"),
    ("es-br", "Spanish (Brazil)"),
    ("es-bz", "Spanish (Belize)"),
    ("es-cl", "Spanish (Chile)"),
    ("es-co", "Spanish (Colombia)"),
    ("es-cr", "Spanish (Costa Rica)"),
    ("es-cu", "Spanish (Cuba)"),
    ("es-do", "Spanish (Dominican Republic)"),
    ("es-ea", "Spanish (Ceuta & Melilla)"),
    ("es-ec", "Spanish (Ecuador)"),
    ("es-es", "Spanish (Spain)"),
    ("es-gq", "Spanish (Equatorial Guinea)"),
    ("es-gt", "Spanish (Guatemala)"),
    ("es-hn", "Spanish (Honduras)"),
    ("es-ic", "Spanish (Canary Islands)"),
    ("es-mx", "Spanish (Mexico)"),
    ("es-ni", "Spanish (Nicaragua)"),
    ("es-pa", "Spanish (Panama)"),
    ("es-pe", "Spanish (Peru)"),
    ("es-ph", "Spanish (Philippines)"),
    ("es-pr", "Spanish (Puerto Rico)"),
    ("es-py", "Spanish (Paraguay)"),
    ("es-sv", "Spanish (El Salvador)"),
    ("es-us", "Spanish (United States)"),
    ("es-uy", "Spanish (Uruguay)"),
    ("es-ve", "Spanish (Venezuela)"),
    ("et", "Estonian"),
    ("et-ee", "Estonian (Estonia)"),
    ("eu", "Basque"),
    ("eu-es", "Basque (Spain)"),
    ("ewo", "Ewondo"),
    ("ewo-cm", "Ewondo (Cameroon)"),
    ("fa", "Persian"),
    ("fa-af", "Persian (Afghanistan)"),
    ("fa-ir", "Persian (Iran)"),
    ("ff", "Fulah"),
    ("ff-adlm", "Fulah (Adlam)"),
    ("ff-adlm-bf", "Fulah (Adlam, Burkina Faso)"),
    ("ff-adlm-cm", "Fulah (Adlam, Cameroon)"),
    ("ff-adlm-gh", "Fulah (Adlam, Ghana)"),
    ("ff-adlm-gm", "Fulah (Adlam, Gambia)"),
    ("ff-adlm-gn", "Fulah (Adlam, Guinea)"),
    ("ff-adlm-gw", "Fulah (Adlam, Guinea-Bissau)"),
    ("ff-adlm-lr", "Fulah (Adlam, Liberia)"),
    ("ff-adlm-mr", "Fulah (Adlam, Mauritania)"),
    ("ff-adlm-ne", "Fulah (Adlam, Niger)"),
    ("ff-adlm-ng", "Fulah (Adlam, Nigeria)"),
    ("ff-adlm-sl", "Fulah (Adlam, Sierra Leone)"),
    ("ff-adlm-sn", "Fulah (Adlam, Senegal)"),
    ("ff-latn", "Fulah (Latin)"),
    ("ff-latn-bf", "Fulah (Latin, Burkina Faso)"),
    ("ff-latn-cm", "Fulah (Latin, Cameroon)"),
    ("ff-latn-gh", "Fulah (Latin, Ghana)"),
    ("ff-latn-gm", "Fulah (Latin, Gambia)"),
    ("ff-latn-gn", "Fulah (Latin, Guinea)"),
    ("ff-latn-gw", "Fulah (Latin, Guinea-Bissau)"),
    ("ff-latn-lr", "Fulah (Latin, Liberia)"),
    ("ff-latn-mr", "Fulah (Latin, Mauritania)"),
    ("ff-latn-ne", "Fulah (Latin, Niger)"),
    ("ff-latn-ng", "Fulah (Latin, Nigeria)"),
    ("ff-latn-sl", "Fulah (Latin, Sierra Leone)"),
    ("ff-latn-sn", "Fulah (Latin, Senegal)"),
    ("fi", "Finnish"),
    ("fi-fi", "Finnish (Finland)"),
    ("fil", "Filipino"),
    ("fil-ph", "Filipino (Philippines)"),
    ("fo", "Faroese"),
    ("fo-dk", "Faroese (Denmark)"),
    ("fo-fo", "Faroese (Faroe Islands)"),
    ("fr", "French"),
    ("fr-be", "French (Belgium)"),
    ("fr-bf", "French (Burkina Faso)"),
    ("fr-bi", "French (Burundi)"),
    ("fr-bj", "French (Benin)"),
    ("fr-bl", "French (St. Barthélemy)"),
    ("fr-ca", "French (Canada)"),
    ("fr-cd", "French (Congo - Kinshasa)"),
    ("fr-cf", "French (Central African Republic)"),
    ("fr-cg", "French (Congo - Brazzaville)"),
    ("fr-ch", "French (Switzerland)"),
    ("fr-ci", "French (Côte d’Ivoire)"),
    ("fr-cm", "French (Cameroon)"),
    ("fr-dj", "French (Djibouti)"),
    ("fr-dz", "French (Algeria)"),
    ("fr-fr", "French (France)"),
    ("fr-ga", "French (Gabon)"),
    ("fr-gf", "French (French Guiana)"),
    ("fr-gn", "French (Guinea)"),
    ("fr-gp", "French (Guadeloupe)"),
    ("fr-gq", "French (Equatorial Guinea)"),
    ("fr-ht", "French (Haiti)"),
    ("fr-km", "French (Comoros)"),
    ("fr-lu", "French (Luxembourg)"),
    ("fr-ma", "French (Morocco)"),
    ("fr-mc", "French (Monaco)"),
    ("fr-mf", "French (St. Martin)"),
    ("fr-mg", "French (Madagascar)"),
    ("fr-ml", "French (Mali)"),
    ("fr-mq", "French (Martinique)"),
    ("fr-mr", "French (Mauritania)"),
    ("fr-mu", "French (Mauritius)"),
    ("fr-nc", "French (New Caledonia)"),
    ("fr-ne", "French (Niger)"),
    ("fr-pf", "French (French Polynesia)"),
    ("fr-pm", "French (St. Pierre & Miquelon)"),
    ("fr-re", "French (Réunion)"),
    ("fr-rw", "French (Rwanda)"),
    ("fr-sc", "French (Seychelles)"),
    ("fr-sn", "French (Senegal)"),
    ("fr-sy", "French (Syria)"),
    ("fr-td", "French (Chad)"),
    ("fr-tg", "French (Togo)"),
    ("fr-tn", "French (Tunisia)"),
    ("fr-vu", "French (Vanuatu)"),
    ("fr-wf", "French (Wallis & Futuna)"),
    ("fr-yt", "French (Mayotte)"),
    ("fur", "Friulian"),
    ("fur-it", "Friulian (Italy)"),
    ("fy", "Western Frisian"),
    ("fy-nl", "Western Frisian (Netherlands)"),
    ("ga", "Irish"),
    ("ga-gb", "Irish (United Kingdom)"),
    ("ga-ie", "Irish (Ireland)"),
    ("gd", "Scottish Gaelic"),
    ("gd-gb", "Scottish Gaelic (United Kingdom)"),
    ("gl", "Galician"),
    ("gl-es", "Galician (Spain)"),
    ("gsw", "Swiss German"),
    ("gsw-ch", "Swiss German (Switzerland)"),
    ("gsw-fr", "Swiss German (France)"),
    ("gsw-li", "Swiss German (Liechtenstein)"),
    ("gu", "Gujarati"),
    ("gu-in", "Gujarati (India)"),
    ("guz", "Gusii"),
    ("guz-ke", "Gusii (Kenya)"),
    ("gv", "Manx"),
    ("gv-im", "Manx (Isle of Man)"),
    ("ha", "Hausa"),
    ("ha-gh", "Hausa (Ghana)"),
    ("ha-ne", "Hausa (Niger)"),
    ("ha-ng", "Hausa (Nigeria)"),
    ("haw", "Hawaiian"),
    ("haw-us", "Hawaiian (United States)"),
    ("he", "Hebrew"),
    ("he-il", "Hebrew (Israel)"),
    ("hi", "Hindi"),
    ("hi-in", "Hindi (India)"),
    ("hr", "Croatian"),
    ("hr-ba", "Croatian (Bosnia & Herzegovina)"),
    ("hr-hr", "Croatian (Croatia)"),
    ("hsb", "Upper Sorbian"),
    ("hsb-de", "Upper Sorbian (Germany)"),
    ("hu", "Hungarian"),
    ("hu-hu", "Hungarian (Hungary)"),
    ("hy", "Armenian"),
    ("hy-am", "Armenian (Armenia)"),
    ("ia", "Interlingua"),
    ("id", "Indonesian"),
    ("id-id", "Indonesian (Indonesia)"),
    ("ig", "Igbo"),
    ("ig-ng", "Igbo (Nigeria)"),
    ("ii", "Sichuan Yi"),
    ("ii-cn", "Sichuan Yi (China)"),
    ("is", "Icelandic"),
    ("is-is", "Icelandic (Iceland)"),
    ("it", "Italian"),
    ("it-ch", "Italian (Switzerland)"),
    ("it-it", "Italian (Italy)"),
    ("it-sm", "Italian (San Marino)"),
    ("it-va", "Italian (Vatican City)"),
    ("ja", "Japanese"),
    ("ja-jp", "Japanese (Japan)"),
    ("jgo", "Ngomba"),
    ("jgo-cm", "Ngomba (Cameroon)"),
    ("jmc", "Machame"),
    ("jmc-tz", "Machame (Tanzania)"),
    ("jv", "Javanese"),
    ("jv-id", "Javanese (Indonesia)"),
    ("ka", "Georgian"),
    ("ka-ge", "Georgian (Georgia)"),
    ("kab", "Kabyle"),
    ("kab-dz", "Kabyle (Algeria)"),
    ("kam", "Kamba"),
    ("kam-ke", "Kamba (Kenya)"),
    ("kde", "Makonde"),
    ("kde-tz", "Makonde (Tanzania)"),
    ("kea", "Kabuverdianu"),
    ("kea-cv", "Kabuverdianu (Cape Verde)"),
    ("khq", "Koyra Chiini"),
    ("khq-ml", "Koyra Chiini (Mali)"),
    ("ki", "Kikuyu"),
    ("ki-ke", "Kikuyu (Kenya)"),
    ("kk", "Kazakh"),
    ("kk-kz", "Kazakh (Kazakhstan)"),
    ("kkj", "Kako"),
    ("kkj-cm", "Kako (Cameroon)"),
    ("kl", "Kalaallisut"),
    ("kl-gl", "Kalaallisut (Greenland)"),
    ("kln", "Kalenjin"),
    ("kln-ke", "Kalenjin (Kenya)"),
    ("km", "Khmer"),
    ("km-kh", "Khmer (Cambodia)"),
    ("kn", "Kannada"),
    ("kn-in", "Kannada (India)"),
    ("ko", "Korean"),
    ("ko-kp", "Korean (North Korea)"),
    ("ko-kr", "Korean (South Korea)"),
    ("kok", "Konkani"),
    ("kok-in", "Konkani (India)"),
    ("ks", "Kashmiri"),
    ("ks-arab", "Kashmiri (Arabic)"),
    ("ks-arab-in", "Kashmiri (Arabic, India)"),
    ("ksb", "Shambala"),
    ("ksb-tz", "Shambala (Tanzania)"),
    ("ksf", "Bafia"),
    ("ksf-cm", "Bafia (Cameroon)"),
    ("ksh", "Colognian"),
    ("ksh-de", "Colognian (Germany)"),
    ("ku", "Kurdish"),
    ("ku-tr", "Kurdish (Turkey)"),
    ("kw", "Cornish"),
    ("kw-gb", "Cornish (United Kingdom)"),
    ("ky", "Kyrgyz"),
    ("ky-kg", "Kyrgyz (Kyrgyzstan)"),
    ("lag", "Langi"),
    ("lag-tz", "Langi (Tanzania)"),
    ("lb", "Luxembourgish"),
    ("lb-lu", "Luxembourgish (Luxembourg)"),
    ("lg", "Ganda"),
    ("lg-ug", "Ganda (Uganda)"),
    ("lkt", "Lakota"),
    ("lkt-us", "Lakota (United States)"),
    ("ln", "Lingala"),
    ("ln-ao", "Lingala (Angola)"),
    ("ln-cd", "Lingala (Congo - Kinshasa)"),
    ("ln-cf", "Lingala (Central African Republic)"),
    ("ln-cg", "Lingala (Congo - Brazzaville)"),
    ("lo", "Lao"),
    ("lo-la", "Lao (Laos)"),
    ("lrc", "Northern Luri"),
    ("lrc-iq", "Northern Luri (Iraq)"),
    ("lrc-ir", "Northern Luri (Iran)"),
    ("lt", "Lithuanian"),
    ("lt-lt", "Lithuanian (Lithuania)"),
    ("lu", "Luba-Katanga"),
    ("lu-cd", "Luba-Katanga (Congo - Kinshasa)"),
    ("luo", "Luo"),
    ("luo-ke", "Luo (Kenya)"),
    ("luy", "Luyia"),
    ("luy-ke", "Luyia (Kenya)"),
    ("lv", "Latvian"),
    ("lv-lv", "Latvian (Latvia)"),
    ("mai", "Maithili"),
    ("mai-in", "Maithili (India)"),
    ("mas", "Masai"),
    ("mas-ke", "Masai (Kenya)"),
    ("mas-tz", "Masai (Tanzania)"),
    ("mer", "Meru"),
    ("mer-ke", "Meru (Kenya)"),
    ("mfe", "Morisyen"),
    ("mfe-mu", "Morisyen (Mauritius)"),
    ("mg", "Malagasy"),
    ("mg-mg", "Malagasy (Madagascar)"),
    ("mgh", "Makhuwa-Meetto"),
    ("mgh-mz", "Makhuwa-Meetto (Mozambique)"),
    ("mgo", "Metaʼ"),
    ("mgo-cm", "Metaʼ (Cameroon)"),
    ("mi", "Maori"),
    ("mi-nz", "Maori (New Zealand)"),
    ("mk", "Macedonian"),
    ("mk-mk", "Macedonian (North Macedonia)"),
    ("ml", "Malayalam"),
    ("ml-in", "Malayalam (India)"),
    ("mn", "Mongolian"),
    ("mn-mn", "Mongolian (Mongolia)"),
    ("mni", "Manipuri"),
    ("mni-beng", "Manipuri (Bangla)"),
    ("mni-beng-in", "Manipuri (Bangla, India)"),
    ("mr", "Marathi"),
    ("mr-in", "Marathi (India)"),
    ("ms", "Malay"),
    ("ms-bn", "Malay (Brunei)"),
    ("ms-id", "Malay (Indonesia)"),
    ("ms-my", "Malay (Malaysia)"),
    ("ms-sg", "Malay (Singapore)"),
    ("mt", "Maltese"),
    ("mt-mt", "Maltese (Malta)"),
    ("mua", "Mundang"),
    ("mua-cm", "Mundang (Cameroon)"),
    ("my", "Burmese"),
    ("my-mm", "Burmese (Myanmar (Burma))"),
    ("mzn", "Mazanderani"),
    ("mzn-ir", "Mazanderani (Iran)"),
    ("naq", "Nama"),
    ("naq-na", "Nama (Namibia)"),
    ("nb", "Norwegian Bokmål"),
    ("nb-no", "Norwegian Bokmål (Norway)"),
    ("nb-sj", "Norwegian Bokmål (Svalbard & Jan Mayen)"),
    ("nd", "North Ndebele"),
    ("nd-zw", "North Ndebele (Zimbabwe)"),
    ("nds", "Low German"),
    ("nds-de", "Low German (Germany)"),
    ("nds-nl", "Low German (Netherlands)"),
    ("ne", "Nepali"),
    ("ne-in", "Nepali (India)"),
    ("ne-np", "Nepali (Nepal)"),
    ("nl", "Dutch"),
    ("nl-aw", "Dutch (Aruba)"),
    ("nl-be", "Dutch (Belgium)"),
    ("nl-bq", "Dutch (Caribbean Netherlands)"),
    ("nl-cw", "Dutch (Curaçao)"),
    ("nl-nl", "Dutch (Netherlands)"),
    ("nl-sr", "Dutch (Suriname)"),
    ("nl-sx", "Dutch (Sint Maarten)"),
    ("nmg", "Kwasio"),
    ("nmg-cm", "Kwasio (Cameroon)"),
    ("nn", "Norwegian Nynorsk"),
    ("nn-no", "Norwegian Nynorsk (Norway)"),
    ("nnh", "Ngiemboon"),
    ("nnh-cm", "Ngiemboon (Cameroon)"),
    ("nus", "Nuer"),
    ("nus-ss", "Nuer (South Sudan)"),
    ("nyn", "Nyankole"),
    ("nyn-ug", "Nyankole (Uganda)"),
    ("om", "Oromo"),
    ("om-et", "Oromo (Ethiopia)"),
    ("om-ke", "Oromo (Kenya)"),
    ("or", "Odia"),
    ("or-in", "Odia (India)"),
    ("os", "Ossetic"),
    ("os-ge", "Ossetic (Georgia)"),
    ("os-ru", "Ossetic (Russia)"),
    ("pa", "Punjabi"),
    ("pa-arab", "Punjabi (Arabic)"),
    ("pa-arab-pk", "Punjabi (Arabic, Pakistan)"),
    ("pa-guru", "Punjabi (Gurmukhi)"),
    ("pa-guru-in", "Punjabi (Gurmukhi, India)"),
    ("pcm", "Nigerian Pidgin"),
    ("pcm-ng", "Nigerian Pidgin (Nigeria)"),
    ("pl", "Polish"),
    ("pl-pl", "Polish (Poland)"),
    ("prg", "Prussian"),
    ("ps", "Pashto"),
    ("ps-af", "Pashto (Afghanistan)"),
    ("ps-pk", "Pashto (Pakistan)"),
    ("pt", "Portuguese"),
    ("pt-ao", "Portuguese (Angola)"),
    ("pt-br", "Portuguese (Brazil)"),
    ("pt-ch", "Portuguese (Switzerland)"),
    ("pt-cv", "Portuguese (Cape Verde)"),
    ("pt-gq", "Portuguese (Equatorial Guinea)"),
    ("pt-gw", "Portuguese (Guinea-Bissau)"),
    ("pt-lu", "Portuguese (Luxembourg)"),
    ("pt-mo", "Portuguese (Macao SAR China)"),
    ("pt-mz", "Portuguese (Mozambique)"),
    ("pt-pt", "Portuguese (Portugal)"),
    ("pt-st", "Portuguese (São Tomé & Príncipe)"),
    ("pt-tl", "Portuguese (Timor-Leste)"),
    ("qu", "Quechua"),
    ("qu-bo", "Quechua (Bolivia)"),
    ("qu-ec", "Quechua (Ecuador)"),
    ("qu-pe", "Quechua (Peru)"),
    ("rm", "Romansh"),
    ("rm-ch", "Romansh (Switzerland)"),
    ("rn", "Rundi"),
    ("rn-bi", "Rundi (Burundi)"),
    ("ro", "Romanian"),
    ("ro-md", "Romanian (Moldova)"),
    ("ro-ro", "Romanian (Romania)"),
    ("rof", "Rombo"),
    ("rof-tz", "Rombo (Tanzania)"),
    ("ru", "Russian"),
    ("ru-by", "Russian (Belarus)"),
    ("ru-kg", "Russian (Kyrgyzstan)"),
    ("ru-kz", "Russian (Kazakhstan)"),
    ("ru-md", "Russian (Moldova)"),
    ("ru-ru", "Russian (Russia)"),
    ("ru-ua", "Russian (Ukraine)"),
    ("rw", "Kinyarwanda"),
    ("rw-rw", "Kinyarwanda (Rwanda)"),
    ("rwk", "Rwa"),
    ("rwk-tz", "Rwa (Tanzania)"),
    ("sah", "Sakha"),
    ("sah-ru", "Sakha (Russia)"),
    ("saq", "Samburu"),
    ("saq-ke", "Samburu (Kenya)"),
    ("sat", "Santali"),
    ("sat-olck", "Santali (Ol Chiki)"),
    ("sat-olck-in", "Santali (Ol Chiki, India)"),
    ("sbp", "Sangu"),
    ("sbp-tz", "Sangu (Tanzania)"),
    ("sd", "Sindhi"),
    ("sd-arab", "Sindhi (Arabic)"),
    ("sd-arab-pk", "Sindhi (Arabic, Pakistan)"),
    ("sd-deva", "Sindhi (Devanagari)"),
    ("sd-deva-in", "Sindhi (Devanagari, India)"),
    ("se", "Northern Sami"),
    ("se-fi", "Northern Sami (Finland)"),
    ("se-no", "Northern Sami (Norway)"),
    ("se-se", "Northern Sami (Sweden)"),
    ("seh", "Sena"),
    ("seh-mz", "Sena (Mozambique)"),
    ("ses", "Koyraboro Senni"),
    ("ses-ml", "Koyraboro Senni (Mali)"),
    ("sg", "Sango"),
    ("sg-cf", "Sango (Central African Republic)"),
    ("shi", "Tachelhit"),
    ("shi-latn", "Tachelhit (Latin)"),
    ("shi-latn-ma", "Tachelhit (Latin, Morocco)"),
    ("shi-tfng", "Tachelhit (Tifinagh)"),
    ("shi-tfng-ma", "Tachelhit (Tifinagh, Morocco)"),
    ("si", "Sinhala"),
    ("si-lk", "Sinhala (Sri Lanka)"),
    ("sk", "Slovak"),
    ("sk-sk", "Slovak (Slovakia)"),
    ("sl", "Slovenian"),
    ("sl-si", "Slovenian (Slovenia)"),
    ("smn", "Inari Sami"),
    ("smn-fi", "Inari Sami (Finland)"),
    ("sn", "Shona"),
    ("sn-zw", "Shona (Zimbabwe)"),
    ("so", "Somali"),
    ("so-dj", "Somali (Djibouti)"),
    ("so-et", "Somali (Ethiopia)"),
    ("so-ke", "Somali (Kenya)"),
    ("so-so", "Somali (Somalia)"),
    ("sq", "Albanian"),
    ("sq-al", "Albanian (Albania)"),
    ("sq-mk", "Albanian (North Macedonia)"),
    ("sq-xk", "Albanian (Kosovo)"),
    ("sr", "Serbian"),
    ("sr-cyrl", "Serbian (Cyrillic)"),
    ("sr-cyrl-ba", "Serbian (Cyrillic, Bosnia & Herzegovina)"),
    ("sr-cyrl-me", "Serbian (Cyrillic, Montenegro)"),
    ("sr-cyrl-rs", "Serbian (Cyrillic, Serbia)"),
    ("sr-cyrl-xk", "Serbian (Cyrillic, Kosovo)"),
    ("sr-latn", "Serbian (Latin)"),
    ("sr-latn-ba", "Serbian (Latin, Bosnia & Herzegovina)"),
    ("sr-latn-me", "Serbian (Latin, Montenegro)"),
    ("sr-latn-rs", "Serbian (Latin, Serbia)"),
    ("sr-latn-xk", "Serbian (Latin, Kosovo)"),
    ("su", "Sundanese"),
    ("su-latn", "Sundanese (Latin)"),
    ("su-latn-id", "Sundanese (Latin, Indonesia)"),
    ("sv", "Swedish"),
    ("sv-ax", "Swedish (Åland Islands)"),
    ("sv-fi", "Swedish (Finland)"),
    ("sv-se", "Swedish (Sweden)"),
    ("sw", "Swahili"),
    ("sw-cd", "Swahili (Congo - Kinshasa)"),
    ("sw-ke", "Swahili (Kenya)"),
    ("sw-tz", "Swahili (Tanzania)"),
    ("sw-ug", "Swahili (Uganda)"),
    ("ta", "Tamil"),
    ("ta-in", "Tamil (India)"),
    ("ta-lk", "Tamil (Sri Lanka)"),
    ("ta-my", "Tamil (Malaysia)"),
    ("ta-sg", "Tamil (Singapore)"),
    ("te", "Telugu"),
    ("te-in", "Telugu (India)"),
    ("teo", "Teso"),
    ("teo-ke", "Teso (Kenya)"),
    ("teo-ug", "Teso (Uganda)"),
    ("tg", "Tajik"),
    ("tg-tj", "Tajik (Tajikistan)"),
    ("th", "Thai"),
    ("th-th", "Thai (Thailand)"),
    ("ti", "Tigrinya"),
    ("ti-er", "Tigrinya (Eritrea)"),
    ("ti-et", "Tigrinya (Ethiopia)"),
    ("tk", "Turkmen"),
    ("tk-tm", "Turkmen (Turkmenistan)"),
    ("to", "Tongan"),
    ("to-to", "Tongan (Tonga)"),
    ("tr", "Turkish"),
    ("tr-cy", "Turkish (Cyprus)"),
    ("tr-tr", "Turkish (Turkey)"),
    ("tt", "Tatar"),
    ("tt-ru", "Tatar (Russia)"),
    ("twq", "Tasawaq"),
    ("twq-ne", "Tasawaq (Niger)"),
    ("tzm", "Central Atlas Tamazight"),
    ("tzm-ma", "Central Atlas Tamazight (Morocco)"),
    ("ug", "Uyghur"),
    ("ug-cn", "Uyghur (China)"),
    ("uk", "Ukrainian"),
    ("uk-ua", "Ukrainian (Ukraine)"),
    ("ur", "Urdu"),
    ("ur-in", "Urdu (India)"),
    ("ur-pk", "Urdu (Pakistan)"),
    ("uz", "Uzbek"),
    ("uz-arab", "Uzbek (Arabic)"),
    ("uz-arab-af", "Uzbek (Arabic, Afghanistan)"),
    ("uz-cyrl", "Uzbek (Cyrillic)"),
    ("uz-cyrl-uz", "Uzbek (Cyrillic, Uzbekistan)"),
    ("uz-latn", "Uzbek (Latin)"),
    ("uz-latn-uz", "Uzbek (Latin, Uzbekistan)"),
    ("vai", "Vai"),
    ("vai-latn", "Vai (Latin)"),
    ("vai-latn-lr", "Vai (Latin, Liberia)"),
    ("vai-vaii", "Vai (Vai)"),
    ("vai-vaii-lr", "Vai (Vai, Liberia)"),
    ("vi", "Vietnamese"),
    ("vi-vn", "Vietnamese (Vietnam)"),
    ("vo", "Volapük"),
    ("vun", "Vunjo"),
    ("vun-tz", "Vunjo (Tanzania)"),
    ("wae", "Walser"),
    ("wae-ch", "Walser (Switzerland)"),
    ("wo", "Wolof"),
    ("wo-sn", "Wolof (Senegal)"),
    ("xh", "Xhosa"),
    ("xh-za", "Xhosa (South Africa)"),
    ("xog", "Soga"),
    ("xog-ug", "Soga (Uganda)"),
    ("yav", "Yangben"),
    ("yav-cm", "Yangben (Cameroon)"),
    ("yi", "Yiddish"),
    ("yo", "Yoruba"),
    ("yo-bj", "Yoruba (Benin)"),
    ("yo-ng", "Yoruba (Nigeria)"),
    ("yue", "Cantonese"),
    ("yue-hans", "Cantonese (Simplified)"),
    ("yue-hans-cn", "Cantonese (Simplified, China)"),
    ("yue-hant", "Cantonese (Traditional)"),
    ("yue-hant-hk", "Cantonese (Traditional, Hong Kong SAR China)"),
    ("zgh", "Standard Moroccan Tamazight"),
    ("zgh-ma", "Standard Moroccan Tamazight (Morocco)"),
    ("zh", "Chinese"),
    ("zh-hans", "Chinese (Simplified)"),
    ("zh-hans-cn", "Chinese (Simplified, China)"),
    ("zh-hans-hk", "Chinese (Simplified, Hong Kong SAR China)"),
    ("zh-hans-mo", "Chinese (Simplified, Macao SAR China)"),
    ("zh-hans-sg", "Chinese (Simplified, Singapore)"),
    ("zh-hant", "Chinese (Traditional)"),
    ("zh-hant-hk", "Chinese (Traditional, Hong Kong SAR China)"),
    ("zh-hant-mo", "Chinese (Traditional, Macao SAR China)"),
    ("zh-hant-tw", "Chinese (Traditional, Taiwan)"),
    ("zu", "Zulu"),
    ("zu-za", "Zulu (South Africa)"),
]
