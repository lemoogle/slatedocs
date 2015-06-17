{u'enum_documentation': {u'processing': {u'description': u'Include Connector runs that are in the Processing state.', u'label': u'Processing status'}, u'finished': {u'description': u'Include Connector runs that are in the Finished state.', u'label': u'Finished status'}, u'stopped': {u'description': u'Include Connector runs that are in the Stopped state.', u'label': u'Stopped status'}, u'error': {u'description': u'Include Connector runs that are in the Error state.', u'label': u'Error status'}, u'stopping': {u'description': u'Include Connector runs that are in the Stopping state.', u'label': u'Stopping status'}, u'queued': {u'description': u'Include Connector runs that are in the Queued state.', u'label': u'Queued status'}}, u'enum': [u'queued', u'processing', u'finished', u'error', u'stopping', u'stopped'], u'type': u'string'}
{u'enum_documentation': {u'driverslicense_us': {u'description': u"Matches driver's license numbers for each US state. For example, F255-123-45-678-0.", u'label': u'US Drivers License Numbers'}, u'pii': {u'description': u'A superset entity type that aggregates the address, phone number, credit card, full person name, IP address, e-mail address, Social Security and National Insurance entity types.', u'label': u'Personal Identifying Information'}, u'person_fullname_eng': {u'description': u'Matches multiple person name as components in pairs or longer strings, such as Firstname Lastname, Lastname Suffix, Firstname nee Lastname. For example, Agnes (nee Kozell).', u'label': u'English Full Person Name'}, u'bankaccount_ca': {u'description': u'Matches Canadian bank account numbers. For example, 123-123456-789.', u'label': u'Canadian Bank Account Numbers'}, u'licenseplate_us': {u'description': u'Matches vehicle license plate numbers for all US states. For example, ABC D12.', u'label': u'US Vehicle License Plates'}, u'address_zh': {u'description': u'Matches Chinese addresses in both Simplified Chinese and English. For example, \u6b66\u6c49\u5e02\u6c49\u53e3\u5efa\u8bbe\u5927\u9053568\u53f7\u65b0\u4e16\u754c\u56fd\u8d38\u5927\u53a6I\u5ea79\u697c910\u5ba4.', u'label': u'Chinese Addresses'}, u'date_eng': {u'description': u'Matches English dates, including month names (long and short forms), days of the week, years,times of the day, and dates formed from a combination of these formats. It also matches days and periods relative to the current date, and season names. For example, Saturday, January 5th, 2008.', u'label': u'English Dates'}, u'number_phone_ca': {u'description': u'Matches Canadian phone numbers, in undelimited forms or using spaces, hyphens, or dots as delimiters. It includes alphanumeric phone numbers. For example, 867-920-9209.', u'label': u'Canadian Phone Numbers'}, u'driverslicense_fr': {u'description': u"Matches driver's license numbers for France. For example, 010123456789.", u'label': u'French Drivers License Numbers'}, u'socialsecurity_us': {u'description': u'Matches US Social Security numbers, in undelimited forms or using hyphens or spaces as delimiters. For example, 354 81 9114.', u'label': u'US Social Security Numbers'}, u'number_phone_au': {u'description': u'Matches Australian landline, mobile and other phone numbers. For example, +61 3 34 45 56 67.', u'label': u'Australian Phone Numbers'}, u'licenseplate_ca': {u'description': u'Matches vehicle license plate numbers for all Canadian provinces. For example, ABC-1234.', u'label': u'Canadian Vehicle License Plates'}, u'address_it': {u'description': u'Matches Itallian addresses. For example, Strada del Masarone 67, 13900 Biella (MI).', u'label': u'Italian Addresses'}, u'address_gb': {u'description': u'Matches UK addresses. For example, Unit D, Acorn Business Park, Ling Road, Tower Park, Poole, Dorset, BH12 4NZ.', u'label': u'UK Addresses'}, u'date_fre': {u'description': u'Matches French dates, including month names (long and short forms), days of the week, years,times of the day, and dates formed from a combination of these formats. It also matches days and periods relative to the current date, and season names. For example, Samedi, 5 Janvier, 2008.', u'label': u'French Dates'}, u'people_eng': {u'description': u'Matches the names of over 43,000 famous people from the present day and history. For example, Barack Obama.', u'label': u'English Notable People'}, u'bankaccount_gb': {u'description': u'Matches UK bank account numbers. The account numbers must include a sort code. For example, 60-16-13 31926819.', u'label': u'UK Bank Account Numbers'}, u'licenseplate_gb': {u'description': u'Matches vehicle registration numbers for the UK. Matches are case sensitive (all letters must be in upper case to match). For example, AB07 XYZ.', u'label': u'UK Vehicle License Plates'}, u'date_ger': {u'description': u'Matches German dates, including month names (long and short forms), days of the week, years,times of the day, and dates formed from a combination of these formats. It also matches days and periods relative to the current date, and season names. For example, Samstag, 5. Januar, 2008.', u'label': u'German Dates'}, u'universities': {u'description': u'Institutions of higher eduction.', u'label': u'Universities'}, u'number_cc': {u'description': u'Matches 12 to 19 digit credit card numbers, in undelimited forms or using hyphens or spaces as delimiters. For example, 3799 123456 78901.', u'label': u'Credit Card Numbers'}, u'number_phone_es': {u'description': u'Matches Spanish phone numbers, in undelimited forms or using spaces, hyphens, or dots as delimiters. It includes alphanumeric phone numbers. For example, (+34) 942 733 625.', u'label': u'Spanish Phone Numbers'}, u'socialinsurance_ca': {u'description': u'Matches Canadian Social Insurance numbers, in undelimited forms or using hyphens or spaces as delimiters. For example, 123-456-789.', u'label': u'Canadian Social Insurance Numbers'}, u'pii_ext': {u'description': u'A extended PII superset that in addition to the types matched by the PII type, also includes the bank account and driving license (US-excluded) entity types.', u'label': u'Extended Personal Identifying Information'}, u'profanities': {u'description': u'Offensive words.', u'label': u'Profanities'}, u'licenseplate_de': {u'description': u'Matches vehicle number plates for Germany. For example, AB CD 1234.', u'label': u'German Vehicle License Plates'}, u'number_phone_it': {u'description': u'Matches Italian phone numbers, in undelimited forms or using spaces, hyphens, or dots as delimiters. It includes alphanumeric phone numbers. For example, 03 9494 4949.', u'label': u'Italian Phone Numbers'}, u'bankaccount_us': {u'description': u'Matches US bank account numbers. For example, 15-1234/6226 1234567890.', u'label': u'US Bank Account Numbers'}, u'languages': {u'description': u'Matches languages.', u'label': u'Languages'}, u'bankaccount_fr': {u'description': u'Matches French bank account numbers. For example, 20041 01005 0500013M026 06.', u'label': u'French Bank Account Numbers'}, u'bankaccount_ie': {u'description': u'Matches Irish bank account numbers. For example, 93-11-52 12345678.', u'label': u'Irish Bank Account Numbers'}, u'drugs_eng': {u'description': u'Matches pharmaceuticals drug names.', u'label': u'Pharmaceutical Drug Names'}, u'internet': {u'description': u'Matches host names, IP addresses (IPv4, IPv6, and IPv4-mapped), and HTTP and HTTPs addresses. It also matches addresses for other Internet protocols including file, FTP, news, Telnet and Gopher. For example, www.idolondemand.com.', u'label': u'Internet Addresses'}, u'films': {u'description': u'Identifies over 320,000 film titles.', u'label': u'Films'}, u'address_fr': {u'description': u"Matches addresses from France. For example, 3, Avenue Denis Semeria, Saint-Jean-Cap-Ferrat, Provence-Alpes-C\xf4te d'Azur, 06230, France.", u'label': u'French Addresses'}, u'driverslicense_gb': {u'description': u"Matches driver's license numbers for the UK. Matches are case sensitive (all letters must be in upper case to match). For example, ROBIN756024CJ8UL02.", u'label': u'UK Drivers License Numbers'}, u'number_phone_gb': {u'description': u'Matches UK landline, mobile, freephone, and business phone numbers. It can also match area codes. For example, 01223 123456.', u'label': u'UK Phone Numbers'}, u'file_hash': {u'description': u'Matches 32 and 40 digit hexidecimal.', u'label': u'32 and 40 digit hexidecimal file hashes'}, u'address_ca': {u'description': u'Matches Canadian addresses. For example, 240 4th Avenue S.W., Suite 600, Calgary, Alberta T2P 4H4, Canada.', u'label': u'Canadian Addresses'}, u'internet_email': {u'description': u'Matches e-mail addresses. For example, jane.smith@example.com.', u'label': u'Internet E-mail Addresses'}, u'number_phone_de': {u'description': u'Matches German phone numbers, in undelimited forms or using spaces, hyphens, or dots as delimiters. It includes alphanumeric phone numbers. For example, 089 651285-299.', u'label': u'German Phone Numbers'}, u'licenseplate_fr': {u'description': u'Matches vehicle registration numbers for France. For example, 1234 AB 56.', u'label': u'French Vehicle License Plates'}, u'driverslicense_ca': {u'description': u"Matches driver's license numbers for each Canadian province. For example, A1234-12345-67890.", u'label': u'Canadian Drivers License Numbers'}, u'address_us': {u'description': u'Matches US addresses. For example, 30 South Wacker Drive, 22nd Floor, Chicago, IL 60606.', u'label': u'US Addresses'}, u'person_name_component_eng': {u'description': u'Matches individual firstnames and lastnames as commonly found in English speaking countries. For example, Paul.', u'label': u'Person Name components'}, u'address_es': {u'description': u'Matches addresses from Spain. For example, Av. de las Cortes de C\xe1diz, s/n, C. C. El Corte Ingl\xe9s, 11011, C\xe1diz.', u'label': u'Spanish Addresses'}, u'companies_eng': {u'description': u'Matches over 26,000 English company names. For example, Hewlett-Packard.', u'label': u'English Company Names'}, u'number_phone_zh': {u'description': u'Matches Chinese phone numbers, in undelimited forms or using spaces, hyphens, or dots as delimiters. It includes alphanumeric phone numbers. For example, 021 26037128.', u'label': u'Chinese Phone Numbers'}, u'ip_address': {u'description': u'Matches IP addresses (IPv4, IPv6). For example, 192.168.49.50.', u'label': u'Internet IP Addresses'}, u'places_eng': {u'description': u'Matches English place names, and common abbreviations and alternative forms. For example, London. The place names data is compiled from www.geonames.org.', u'label': u'English Place Names'}, u'organizations': {u'description': u'Matches organization names.', u'label': u'Organization Names'}, u'date_spa': {u'description': u'Matches Spanish dates, including month names (long and short forms), days of the week, years,times of the day, and dates formed from a combination of these formats. It also matches days and periods relative to the current date, and season names. For example, Sabado 5 de enero de 2008.', u'label': u'Spanish Dates'}, u'number_phone_fr': {u'description': u'Matches French phone numbers, in undelimited forms or using spaces, hyphens, or dots as delimiters. It includes alphanumeric phone numbers. For example, +33 140633900.', u'label': u'French Phone Numbers'}, u'bankaccount_de': {u'description': u'Matches German bank account numbers. For example, 150-500-12 1234567.', u'label': u'German Bank Account Numbers'}, u'professions': {u'description': u'Matches professions.', u'label': u'Professions'}, u'date_chi': {u'description': u'Matches Chinese (Simplified & Traditional) dates, including month names (long and short forms), days of the week, years,times of the day, and dates formed from a combination of these formats. It also matches days and periods relative to the current date, and season names. For example, \u5341\u4e8c\u6708\u4e8c\u5341\u56db\u65e5\u665a\u4e0a\u516d\u6642.', u'label': u'Chinese Dates'}, u'date_ita': {u'description': u'Matches Italian dates, including month names (long and short forms), days of the week, years,times of the day, and dates formed from a combination of these formats. It also matches days and periods relative to the current date, and season names. For example, sabato 5 di gennaio del 2008.', u'label': u'Italian Dates'}, u'number_phone_us': {u'description': u'Matches US phone numbers, in undelimited forms or using spaces, hyphens, or dots as delimiters. It includes alphanumeric phone numbers. For example, 598-3113 ext. 123.', u'label': u'US Phone Numbers'}, u'nationalinsurance_gb': {u'description': u'Matches UK National Insurance numbers, in undelimited forms or using hyphens or spaces as delimiters. Matches are case sensitive (all letters must be in upper case to match). For example, AB 12 34 56 C.', u'label': u'UK National Insurance Numbers'}, u'address_de': {u'description': u'Matches addresses from Germany. For example, Postfach 10 01 65, 32547, Bad Oeynhausen, GERMANY.', u'label': u'German Addresses'}, u'address_au': {u'description': u'Matches Australian addresses. For example, Shop 17, Winnellie Shopping Centre, 347 Stuart Hwy, Winnellie, NT, 0820.', u'label': u'Australian Addresses'}, u'driverslicense_de': {u'description': u"Matches driver's license numbers for Germany. For example, G1234567890.", u'label': u'German Drivers License Numbers'}}, u'enum': [u'people_eng', u'places_eng', u'companies_eng', u'organizations', u'languages', u'drugs_eng', u'professions', u'universities', u'profanities', u'films', u'address_au', u'address_ca', u'address_de', u'address_es', u'address_fr', u'address_gb', u'address_it', u'address_us', u'address_zh', u'person_fullname_eng', u'person_name_component_eng', u'pii', u'pii_ext', u'number_phone_au', u'number_phone_ca', u'number_phone_gb', u'number_phone_us', u'number_phone_de', u'number_phone_fr', u'number_phone_it', u'number_phone_es', u'number_phone_zh', u'date_eng', u'date_ger', u'date_fre', u'date_ita', u'date_spa', u'date_chi', u'internet', u'internet_email', u'ip_address', u'number_cc', u'nationalinsurance_gb', u'socialsecurity_us', u'socialinsurance_ca', u'licenseplate_us', u'licenseplate_gb', u'licenseplate_fr', u'licenseplate_de', u'licenseplate_ca', u'driverslicense_us', u'driverslicense_gb', u'driverslicense_fr', u'driverslicense_de', u'driverslicense_ca', u'bankaccount_ca', u'bankaccount_fr', u'bankaccount_gb', u'bankaccount_ie', u'bankaccount_us', u'bankaccount_de', u'file_hash'], u'type': u'string'}
{u'enum_documentation': {u'categorization': {u'description': u'Categorization Text Index Flavor.', u'label': u'Categorization'}, u'explorer': {u'description': u'Explorer Text Index Flavor.', u'label': u'Explorer'}, u'web_cloud': {u'description': u'', u'label': u'Cloud Web Connector.'}, u'standard': {u'description': u'Standard Text Index Flavor.', u'label': u'Standard'}, u'querymanipulation': {u'description': u'Querymanipulation Text Index Flavor.', u'label': u'Querymanipulation'}, u'filesystem_onsite': {u'description': u'', u'label': u'OnSite File System Connector.'}, u'custom_fields': {u'description': u'Custom Fields Text Index Flavor.', u'label': u'Custom Fields'}}, u'enum': [u'standard', u'explorer', u'categorization', u'custom_fields', u'querymanipulation', u'web_cloud', u'filesystem_onsite'], u'type': u'string'}
{u'enum_documentation': {u'content': {u'description': u'Text indexes.', u'label': u'Content'}, u'connector': {u'description': u'Connectors used for extracting content from external systems and repositories.', u'label': u'Connector'}}, u'enum': [u'content', u'connector'], u'type': u'string'}
{u'enum_documentation': {u'categorization': {u'description': u'Categorization Text Index Flavor.', u'label': u'Categorization'}, u'explorer': {u'description': u'Explorer Text Index Flavor.', u'label': u'Explorer'}, u'web_cloud': {u'description': u'Cloud-based Web Connector.', u'label': u'Web Cloud Connector'}, u'standard': {u'description': u'Standard Text Index Flavor.', u'label': u'Standard'}, u'querymanipulation': {u'description': u'Querymanipulation Text Index Flavor.', u'label': u'Query Manipulation'}, u'filesystem_onsite': {u'description': u'Onsite File System Connector.', u'label': u'File System Onsite Connector'}, u'custom_fields': {u'description': u'Custom Fields Text Index Flavor.', u'label': u'Custom Fields'}}, u'enum': [u'standard', u'explorer', u'categorization', u'custom_fields', u'querymanipulation', u'web_cloud', u'filesystem_onsite'], u'type': u'string'}
{u'enum_documentation': {u'content': {u'description': u'Text indexes.', u'label': u'Content'}, u'connector': {u'description': u'Connectors used for extracting content from external systems and repositories.', u'label': u'Connector'}}, u'enum': [u'content', u'connector'], u'type': u'string'}
{u'enum_documentation': {u'all': {u'description': u'All supported barcode types.', u'label': u'All'}, u'code-93': {u'description': u'See http://en.wikipedia.org/wiki/Code_93', u'label': u'Code-93 (1D)'}, u'industrial 2/5': {u'description': u'See http://en.wikipedia.org/wiki/Two-out-of-five_code', u'label': u'Industrial 2/5 (1D)'}, u'iata 2/5': {u'description': u'', u'label': u'IATA 2/5 (1D)'}, u'upc-a': {u'description': u'See http://en.wikipedia.org/wiki/Universal_Product_Code', u'label': u'UPC-A (1D)'}, u'matrix 2/5': {u'description': u'See http://www.n-barcode.com/en/shurui/m-25.html', u'label': u'Matrix 2/5 (1D)'}, u'ucc': {u'description': u'See http://en.wikipedia.org/wiki/GS1-128', u'label': u'UCC (1D)'}, u'codabar': {u'description': u'See http://en.wikipedia.org/wiki/Codabar', u'label': u'Codabar (1D)'}, u'code-128': {u'description': u'See http://en.wikipedia.org/wiki/Code_128', u'label': u'Code-128 (1D)'}, u'datalogic 2/5': {u'description': u'', u'label': u'Datalogic 2/5 (1D)'}, u'data matrix': {u'description': u'http://en.wikipedia.org/wiki/Data_Matrix', u'label': u'Data Matrix (2D)'}, u'all1d': {u'description': u'All 1-Dimensional barcode types.', u'label': u'All supported 1D types'}, u'ean-13': {u'description': u'See http://en.wikipedia.org/wiki/International_Article_Number_%28EAN%29', u'label': u'EAN-13 (1D)'}, u'pdf417': {u'description': u'See http://en.wikipedia.org/wiki/PDF417', u'label': u'PDF417 (2D)'}, u'ean-5': {u'description': u'See http://en.wikipedia.org/wiki/EAN_5', u'label': u'EAN-5 (1D)'}, u'ean-2': {u'description': u'See http://http://en.wikipedia.org/wiki/EAN_2', u'label': u'EAN-2 (1D)'}, u'patch code': {u'description': u'', u'label': u'Patch Code (1D)'}, u'ean-8': {u'description': u'See http://en.wikipedia.org/wiki/EAN-8', u'label': u'EAN-8 (1D)'}, u'qr': {u'description': u'See http://en.wikipedia.org/wiki/QR_code', u'label': u'QR Code (2D)'}, u'code-39': {u'description': u'See http://en.wikipedia.org/wiki/Code_39', u'label': u'Code-39 (1D)'}, u'all2d': {u'description': u'All 2-Dimensional barcode types.', u'label': u'All supported 2D types'}, u'ean-128': {u'description': u'See http://en.wikipedia.org/wiki/GS1-128', u'label': u'EAN-128 (1D)'}, u'upc-e': {u'description': u'See http://en.wikipedia.org/wiki/Universal_Product_Code#UPC-E', u'label': u'UPC-E (1D)'}}, u'enum': [u'all', u'all1d', u'all2d', u'codabar', u'code-128', u'code-39', u'code-93', u'datalogic 2/5', u'data matrix', u'ean-128', u'ean-13', u'ean-2', u'ean-5', u'ean-8', u'iata 2/5', u'industrial 2/5', u'matrix 2/5', u'patch code', u'pdf417', u'qr', u'ucc', u'upc-a', u'upc-e'], u'type': u'string'}
{u'enum_documentation': {u'index': {u'description': u'', u'label': u'List field names for index type fields.'}, u'all': {u'description': u'', u'label': u'List all types of field names.'}, u'reference': {u'description': u'', u'label': u'List field names for expire reference type fields.'}, u'numeric': {u'description': u'', u'label': u'List field names for numeric type fields.'}, u'stored': {u'description': u'', u'label': u'List field names for stored type fields.'}, u'autnrank': {u'description': u'', u'label': u'List field names for rank type fields.'}, u'date': {u'description': u'', u'label': u'List field names for date type fields.'}, u'parametric': {u'description': u'', u'label': u'List field names for parametric type fields.'}}, u'enum': [u'index', u'parametric', u'numeric', u'autnrank', u'reference', u'date', u'stored'], u'type': u'string'}
# API Reference


## Add Agent







```python


import requests
url="http://api.idolondemand.com/1/api/sync/addagent/v1"

data=
{
"agent":"myagent",
"training":"mytraining",
"user":"myuser",
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/addagent/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**agent** | string | Name of the agent
**training** | string | Training data
**user** | string | User's email address
**store** | string | Name of the community store



## Add Role







```python


import requests
url="http://api.idolondemand.com/1/api/sync/addrole/v1"

data=
{
"role":"myrole",
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/addrole/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**role** | string | The name of the new role.
**store** | string | The name of the user store that you want to add the role to.



## Add Store







```python


import requests
url="http://api.idolondemand.com/1/api/sync/addstore/v1"

data=
{
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/addstore/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**store** | string | The name of the new user store.



## Add to Text Index







```python


import requests
url="http://api.idolondemand.com/1/api/sync/addtotextindex/v1"

data=
{
"index":"myindex",
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/addtotextindex/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
json |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**index** | string | The text index to add the file to.
additional_metadata | array | A JSON object containing additional metadata to add to the indexed documents. This option does not apply to JSON input. To add metadata for multiple files, specify objects in order, separated by an empty object.
duplicate_mode | string | The method to use to handle duplicate documents.
reference_prefix | array | A string to add to the start of the reference of documents that are extracted from a file. To add a prefix for multiple files, specify prefixes in order, separated by a space.

### Enums

duplicate_mode | Description
--------- | -----------
duplicate | Keep multiple documents with the same reference.
replace | On adding a document, remove all existing documents with the same reference.


## Add User







```python


import requests
url="http://api.idolondemand.com/1/api/sync/adduser/v1"

data=
{
"password":"mypassword",
"email":"myemail",
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/adduser/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**password** | string | The password for the user. IDOL OnDemand stores passwords as a hash using seeded SHA-256.
**email** | string | The e-mail address of the new user.
**store** | string | The name of the user store that you want to add the user to.



## Sentiment Analysis







```python


import requests
url="http://api.idolondemand.com/1/api/sync/analyzesentiment/v1"

data=
{
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/analyzesentiment/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
text |
url |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
language | string | The language of your source text.

### Enums

language | Description
--------- | -----------
ger | German
fre | French
eng | English
chi | Chinese
tur | Turkish
por | Portuguese
ita | Italian
rus | Russian
spa | Spanish
dut | Dutch
cze | Czech


## Assign Role







```python


import requests
url="http://api.idolondemand.com/1/api/sync/assignrole/v1"

data=
{
"role":"myrole",
"user":"myuser",
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/assignrole/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**role** | string | The name of the role to assign to the user.
**user** | string | The name of the user that you want to assign the role to.
**store** | string | The name of the user store.



## Authenticate







```python


import requests
url="http://api.idolondemand.com/1/api/sync/authenticate/v1"

data=
{
"store":"mystore",
"mechanism":"mymechanism",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/authenticate/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
password | string | The password of the user to authenticate.
**store** | string | The name of the user store.
**mechanism** | string | The authentication method to use.
user | string | The e-mail address of the user to authenticate.

### Enums

mechanism | Description
--------- | -----------
simple | Simple authentication


## Cancel Connector Schedule







```python


import requests
url="http://api.idolondemand.com/1/api/sync/cancelconnectorschedule/v1"

data=
{
"connector":"myconnector",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/cancelconnectorschedule/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**connector** | string | The name of the connector to stop.



## Document Categorization







```python


import requests
url="http://api.idolondemand.com/1/api/sync/categorizedocument/v1"

data=
{
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/categorizedocument/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
text |
json |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
index | string | The name of the IDOL OnDemand text index that you want to search for matching categories. This text index must be of the categorization flavor.
max_results | number | The maximum number of categories to return for this document from the total number of results matched.
field_text | string | A field restriction against the categorization index. Typically, this is a match against a Parametric field in the categories.
print | string | The types of fields and content to display in the results.
print_fields | string | The names of fields to print in the results.

### Enums

print | Description
--------- | -----------
fields | Print the fields listed in the print_fields parameter.
all | All fields.
none | Do not print content fields.
reference | Print reference fields.


## Classify Document







```python


import requests
url="http://api.idolondemand.com/1/api/sync/classifydocument/v1"

data=
{
"collection_sequence":"mycollection_sequence",
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/classifydocument/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
url |
json |
reference |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**collection_sequence** | string | A name or id of the collection sequence that the document should be evaluated against.



## Connector History







```python


import requests
url="http://api.idolondemand.com/1/api/sync/connectorhistory/v1"

data=
{
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/connectorhistory/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
absolute_max_results | number | The absolute maximum number of statuses to return.
show_latest_only | boolean | Set to true to return only the latest history.
min_date | string | The earliest date or time of a connector run to return.
tokens | array | The tokens of the connectors to return the status for.
start | number | The number of the first status to display.
connectors | array | The names of the connectors to return the status for.
max_date | string | The latest date or time of a connector run to return.
max_page_results | number | The maximum number of statuses to return from the absolute number of results returned. If you have set the Start parameter, max_page_results sets the number of the last result from the total results set.
statuses | array | The statuses that you want to return.



## Connector Status







```python


import requests
url="http://api.idolondemand.com/1/api/sync/connectorstatus/v1"

data=
{
"connector":"myconnector",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/connectorstatus/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**connector** | string | The name of the connector to return the status for.
schedule_information | boolean | Set to true to return information about the schedule for you connector.



## Create Classification







```python


import requests
url="http://api.idolondemand.com/1/api/sync/createclassificationobjects/v1"

data=
{
"type":"mytype",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/createclassificationobjects/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
additional | object | Specify a JSON object of additional parameters relevant for the type of classification object being added.
**type** | string | The type of classification object.
name | string | The name of the classification object to add.  Does not apply to lexicon_expression type.
description | string | A textual description for the classification object.  Does not apply to lexicon_expression or condition types.

### Enums

type | Description
--------- | -----------
lexicon | Lexicon
collection | Collection
field_source | Field Source
lexicon_expression | Lexicon Expression
condition | Condition
collection_sequence | Collection Sequence


## Create Connector







```python


import requests
url="http://api.idolondemand.com/1/api/sync/createconnector/v1"

data=
{
"destination":"mydestination",
"connector":"myconnector",
"flavor":"myflavor",
"config":"myconfig",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/createconnector/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
description | string | A brief description of the connector.
schedule | object | A JSON string containing the details of the schedule.
**destination** | object | The destination to which the connector must send retrieved data. This value can be either an index or a pipeline.
credentials_license | object | The user credentials-license to verify the validity of the keys for decryption.
**connector** | string | The name of the connector to create.
credentials | object | The user credentials to use to access the source repository.
**flavor** | string | The flavor of the connector to create.
**config** | object | The configuration attributes, defined by attributes.json.

### Enums

flavor | Description
--------- | -----------
web_cloud | Cloud Web Connector.
filesystem_onsite | OnSite Filesystem Connector


## Create Policy







```python


import requests
url="http://api.idolondemand.com/1/api/sync/createpolicyobjects/v1"

data=
{
"additional":"myadditional",
"type":"mytype",
"name":"myname",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/createpolicyobjects/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**additional** | object | Specify a JSON object of additional parameters relevant for the type of policy object being created.
**type** | string | The type of policy object to create.
**name** | string | The name of the policy object to create.
description | string | A description for the policy object to create.

### Enums

type | Description
--------- | -----------
policy | Policy
policy_type | Policy Type


## Create Query Profile







```python


import requests
url="http://api.idolondemand.com/1/api/sync/createqueryprofile/v1"

data=
{
"query_profile":"myquery_profile",
"config":"myconfig",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/createqueryprofile/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**query_profile** | string | The name of the query profile.
**config** | object | The content of the query profile.



## Create Text Index







```python


import requests
url="http://api.idolondemand.com/1/api/sync/createtextindex/v1"

data=
{
"index":"myindex",
"flavor":"myflavor",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/createtextindex/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**index** | string | The name of the index to create
**flavor** | string | The configuration flavor of the text index.
description | string | A brief description of the index.



## Delete Agent







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deleteagent/v1"

data=
{
"agent":"myagent",
"user":"myuser",
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deleteagent/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**agent** | string | Name of the agent
**user** | string | User's email address
**store** | string | Name of the community store



## Delete Classification







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deleteclassificationobjects/v1"

data=
{
"type":"mytype",
"id":"myid",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deleteclassificationobjects/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**type** | string | The type of classification object.
**id** | array | The ids of the object or objects to delete.

### Enums

type | Description
--------- | -----------
lexicon | Lexicon
collection | Collection
field_source | Field Source
lexicon_expression | Lexicon Expression
condition | Condition
collection_sequence | Collection Sequence


## Delete Connector







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deleteconnector/v1"

data=
{
"connector":"myconnector",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deleteconnector/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**connector** | string | The name of the connector to delete.



## Delete from Text Index







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deletefromtextindex/v1"

data=
{
"index":"myindex",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deletefromtextindex/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
index_reference |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**index** | string | The index to delete document from.
delete_all_documents | boolean | Set to true to delete all documents from the text index.



## Delete Policy







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deletepolicyobjects/v1"

data=
{
"type":"mytype",
"id":"myid",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deletepolicyobjects/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**type** | string | The type of policy object to delete.
**id** | array | An array of policy object ids.

### Enums

type | Description
--------- | -----------
policy | Policy
policy_type | Policy Type


## Delete Query Profile







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deletequeryprofile/v1"

data=
{
"query_profile":"myquery_profile",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deletequeryprofile/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**query_profile** | string | The name of the query profile.



## Delete Role







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deleterole/v1"

data=
{
"role":"myrole",
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deleterole/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**role** | string | The name of the role that you want to delete.
**store** | string | The name of the user store.



## Delete Store







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deletestore/v1"

data=
{
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deletestore/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**store** | string | The name of the user store that you want to delete.



## Delete Text Index







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deletetextindex/v1"

data=
{
"index":"myindex",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deletetextindex/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**index** | string | The name of the index to delete.
confirm | string | The confirmation hash key returned after the first request.



## Delete User







```python


import requests
url="http://api.idolondemand.com/1/api/sync/deleteuser/v1"

data=
{
"email":"myemail",
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/deleteuser/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**email** | string | The e-mail address of the user to delete.
**store** | string | Name of the user store.



## Face Detection







```python


import requests
url="http://api.idolondemand.com/1/api/sync/detectfaces/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/detectfaces/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
additional | boolean | Whether to estimate the ages of the faces.



## Expand Container







```python


import requests
url="http://api.idolondemand.com/1/api/sync/expandcontainer/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/expandcontainer/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
url |
reference |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
depth | number | The maximum depth to which to expand nested containers. It cannot be more than five. Values higher than five are truncated.
password | array | Passwords to use to extract the files.



## Expand Terms







```python


import requests
url="http://api.idolondemand.com/1/api/sync/expandterms/v1"

data=
{
"expansion":"myexpansion",
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/expandterms/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
text |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
sort | string | The criteria to use to order the result terms.
max_terms | number | The maximum number of expanded terms or term phrases to return.
**expansion** | string | The method to use to expand the specified term.
stemming | boolean | Set this parameter to false to return the list of terms in their unstemmed form.

### Enums

sort | Description
--------- | -----------
none | No sorting
documents | Number of document occurrences
alphabetical | Alphabetical
expansion | Description
--------- | -----------
wild | Wildcard expansion
fuzzy | Similar spelling
stem | Same stem


## Concept Extraction







```python


import requests
url="http://api.idolondemand.com/1/api/sync/extractconcepts/v1"

data=
{
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/extractconcepts/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
text |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
language | string | The language of the specified terms.
max_results | number | The maximum number of results to return.

### Enums

language | Description
--------- | -----------
ger | German
fre | French
eng | English
chi | Chinese
ita | Italian
spa | Spanish


## Entity Extraction







```python


import requests
url="http://api.idolondemand.com/1/api/sync/extractentities/v1"

data=
{
"entity_type":"myentity_type",
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/extractentities/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
text |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
show_alternatives | boolean | Set to true to return multiple entries when there are multiple matches for a given string. For example London, UK, and London, Ontario.
**entity_type** | array | The type of entity to extract from the specified text.
unique_entities | boolean | Set to true to remove duplicate entity matches.



## Text Extraction







```python


import requests
url="http://api.idolondemand.com/1/api/sync/extracttext/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/extracttext/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
additional_metadata | array | A JSON object containing additional metadata to add to the extracted documents. This option does not apply to JSON input. To add metadata for multiple files, specify objects in order, separated by an empty object.
extract_xmlattributes | boolean | Whether to extract xml attributes from the file.
extract_metadata | boolean | Whether to extract metadata from the file.
extract_text | boolean | Whether to extract text from the file.
password | array | Passwords to use to extract the files.
reference_prefix | array | A string to add to the start of the reference of documents that are extracted from a file. This option does not apply to JSON input. To add a prefix for multiple files, specify prefixes in order, separated by a space.



## Find Related Concepts







```python


import requests
url="http://api.idolondemand.com/1/api/sync/findrelatedconcepts/v1"

data=
{
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/findrelatedconcepts/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
text |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
min_score | number | The minimum percentage relevance that results must have to the query to return.
min_date | string | The earliest creation date or time that a document can have to return as a result.
sample_size | number | The maximum number of documents to use to generate concepts.
max_results | number | The maximum number of related concepts to return.
field_text | string | The fields that result documents must contain, and the conditions that these fields must meet for the documents to return as results.
max_date | string | The latest creation date or time that a document can have to return as a result.
indexes | array | Type the name of one or more IDOL OnDemand text index to return only documents that are stored in these text indexes. You can use the public datasets, or your own text indexes.



## Find Similar







```python


import requests
url="http://api.idolondemand.com/1/api/sync/findsimilar/v1"

data=
{
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/findsimilar/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
text |
file |
url |
index_reference |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
absolute_max_results | number | The absolute maximum number of results to return for this query.
max_page_results | number | The maximum number of results to return for this query from the absolute number of results returned. If you have set the Start parameter, max_page_results sets the maximum number of results to return from the total results set.
end_tag | string | The closing HTML tag to use to highlight a match. If omitted, this is generated automatically from the start_tag.
min_score | number | The minimum percentage relevance that results must have to the query to return.
total_results | boolean | Set to true to return extra information about the total number of result documents, and the total number of documents and document sections in the query databases.
indexes | array | The name of an IDOL OnDemand text index that you want to search for results. You can use the public datasets, or your own text indexes.
start | number | The number of the first document to display.
print | string | The types of fields and content to display in the results.
print_fields | string | The names of fields to print in the results.
sort | string | The criteria to use for the result display order. By default, results are displayed in order of relevance.
min_date | string | The earliest creation date or time that a document can have to return as a result.
field_text | string | The fields that result documents must contain, and the conditions that these fields must meet for the documents to return as results.
query_profile | string | The name of the query profile that you want to apply.
start_tag | string | The opening HTML tag to use to highlight a match.
summary | string | The type of summary to create for result documents.
max_date | string | The latest creation date or time that a document can have to return as a result.
highlight | string | The highlighting option to use for the result text.

### Enums

print | Description
--------- | -----------
all | All fields.
reference | Reference fields.
fields | Print the fields listed in the print_fields parameter.
none | Do not print content fields.
no_results | Do not print results.
date | Date fields.
all_sections | All fields and all sections.
parametric | Parametric fields.
sort | Description
--------- | -----------
autn_rank | Order by the standard relevance adjustment field.
off | No sorting.
reverse_relevance | Relevance order (least relevant first).
date | Date order (most recent first).
relevance | Relevance order (most relevant first).
reverse_date | Date order (oldest first).
summary | Description
--------- | -----------
quick | Quick Summary
concept | Concept Summary
off | No summary
context | Context Summary
highlight | Description
--------- | -----------
terms | Terms that match the query text.
summary_terms | Query terms that occur in summary sentences.
off | No highlighting.
summary_sentences | Summary sentences that contain query terms.
sentences | Sentences that contain query terms.


## Get Content







```python


import requests
url="http://api.idolondemand.com/1/api/sync/getcontent/v1"

data=
{
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/getcontent/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
index_reference |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
print_fields | string | The names of fields to print in the results.
highlight_expression | string | The terms to highlight in the specified text. Separate the terms with spaces, pluses (+) or commas (,).
start_tag | string | The opening HTML tag to use to highlight a link term.
print | string | The types of fields and content to display in the results.
indexes | string | The text index to get content from.
end_tag | string | The closing HTML tag to use to highlight a link term. If omitted, this is generated automatically from the start_tag.

### Enums

print | Description
--------- | -----------
all | All fields
reference | Reference fields
fields | Print the fields listed in the print_fields parameter
none | Do not print content fields
no_results | Do not print results
date | Date fields
all_sections | All fields and all sections
parametric | Parametric fields


## Get Parametric Values







```python


import requests
url="http://api.idolondemand.com/1/api/sync/getparametricvalues/v1"

data=
{
"field_name":"myfield_name",
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/getparametricvalues/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
text |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
sort | string | The criteria to use for the result display order. By default, results are not sorted.
min_score | number | The minimum percentage relevance that results must have to the query to return.
indexes | array | The text index to use to perform the parametric search.
field_text | string | The fields that result documents must contain, and the conditions that these fields must meet for the documents to return as results.
max_values | number | The maximum number of values to be returned for each matched field name. 0 is unlimited.
**field_name** | string | A comma-separated list of field names to return values for.
document_count | boolean | Set to true to show the number of documents that contain a parametric tag value.

### Enums

sort | Description
--------- | -----------
alphabetical | Alphabetical.
off | No sorting
number_increasing | Numeric field value (lowest number first).
number_decreasing | Numeric field value (highest number first).
document_count | Number of matching documents (descending).
reverse_alphabetical | Reverse alphabetical.


## Highlight Text







```python


import requests
url="http://api.idolondemand.com/1/api/sync/highlighttext/v1"

data=
{
"highlight_expression":"myhighlight_expression",
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/highlighttext/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
text |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**highlight_expression** | string | The terms to highlight in the specified text. Separate the terms with spaces, pluses (+) or commas (,).
start_tag | string | The opening HTML tag to use to highlight a link term.
end_tag | string | The closing HTML tag to use to highlight a link term. If omitted, this is generated automatically from the start_tag.



## Language Identification







```python


import requests
url="http://api.idolondemand.com/1/api/sync/identifylanguage/v1"

data=
{
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/identifylanguage/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
url |
text |
reference |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
additional_metadata | boolean | Set to true to get additional metadata information on identified language.



## Index Status







```python


import requests
url="http://api.idolondemand.com/1/api/sync/indexstatus/v1"

data=
{
"index":"myindex",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/indexstatus/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**index** | string | The name of the text index to return the status for.



## List Agents







```python


import requests
url="http://api.idolondemand.com/1/api/sync/listagents/v1"

data=
{
"user":"myuser",
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/listagents/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**user** | string | User's email address
**store** | string | Name of the community store



## List Indexes







```python


import requests
url="http://api.idolondemand.com/1/api/sync/listindexes/v1"

data=
{
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/listindexes/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
flavor | array | Match against particular worker configurations.
type | array | Match against particular worker sub-types.



## List Resources







```python


import requests
url="http://api.idolondemand.com/1/api/sync/listresources/v1"

data=
{
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/listresources/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
flavor | array | Match against particular worker configurations.
type | array | Match against particular worker sub-types.



## List Roles







```python


import requests
url="http://api.idolondemand.com/1/api/sync/listroles/v1"

data=
{
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/listroles/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**store** | string | The name of the user store.



## List Stores







```python


import requests
url="http://api.idolondemand.com/1/api/sync/liststores/v1"

data=
{
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/liststores/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------



## List User Roles







```python


import requests
url="http://api.idolondemand.com/1/api/sync/listuserroles/v1"

data=
{
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/listuserroles/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
roles | string | Boolean expression to filter the roles by.
users | array | Set of users to filter.
**store** | string | Name of the community store



## List Users







```python


import requests
url="http://api.idolondemand.com/1/api/sync/listusers/v1"

data=
{
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/listusers/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**store** | string | The name of the user store.



## OCR Document







```python


import requests
url="http://api.idolondemand.com/1/api/sync/ocrdocument/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/ocrdocument/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
mode | string | The type of image to process.

### Enums

mode | Description
--------- | -----------
document_scan | Scanned image of a document
subtitle | Text superimposed on an image
photo | photo
scene_photo | Photo of a scene containing text
document_photo | Photo of a document
document | document


## Predict







```python


import requests
url="http://api.idolondemand.com/1/api/sync/predict/v1"

data=
{
"service_name":"myservice_name",
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/predict/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
json |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
format | string | The format to use to return the results.
**service_name** | string | The name of the service to use to activate the prediction model on data.

### Enums

format | Description
--------- | -----------
json | JSON
csv | CSV


## Query Text Index







```python


import requests
url="http://api.idolondemand.com/1/api/sync/querytextindex/v1"

data=
{
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/querytextindex/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
text |
url |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
sort | string | The criteria to use for the result display order. By default, results are displayed in order of relevance.
min_score | number | The minimum percentage relevance that results must have to the query to return.
query_profile | string | The name of the query profile that you want to apply.
summary | string | The type of summary to create for result documents.
total_results | boolean | Set to true to return an estimate of the total number of result documents, and the total number of documents and document sections in the query databases.
absolute_max_results | number | The absolute maximum number of results to return for this query.
start_tag | string | The opening HTML tag to use to highlight a match.
min_date | string | The earliest creation date or time that a document can have to return as a result.
indexes | array | The name of an IDOL OnDemand text index that you want to search for results. You can use the public datasets, or your own text indexes.
start | number | The number of the first document to display.
field_text | string | The fields that result documents must contain, and the conditions that these fields must meet for the documents to return as results.
max_date | string | The latest creation date or time that a document can have to return as a result.
max_page_results | number | The maximum number of results to return for this query from the absolute number of results returned. If you have set the Start parameter, max_page_results sets the maximum number of results to return from the total results set.
print | string | The types of fields and content to display in the results.
highlight | string | The highlighting option to use for the result text.
print_fields | string | The names of fields to print in the results.
end_tag | string | The closing HTML tag to use to highlight a match. If omitted, this is generated automatically from the start_tag.

### Enums

sort | Description
--------- | -----------
autn_rank | Order by the standard relevance adjustment field.
off | No sorting.
reverse_relevance | Relevance order (least relevant first).
date | Date order (most recent first).
relevance | Relevance order (most relevant first).
reverse_date | Date order (oldest first).
summary | Description
--------- | -----------
quick | Quick Summary
concept | Concept Summary
off | No summary
context | Context Summary
print | Description
--------- | -----------
all | All fields.
reference | Reference fields.
fields | Print fields listed in the print_fields parameter.
none | Do not print content fields.
no_results | Do not print results.
date | Date fields.
all_sections | All fields and all sections.
parametric | Parametric fields.
highlight | Description
--------- | -----------
terms | Terms that match the query text.
summary_terms | Query terms that occur in summary sentences.
off | No highlighting.
summary_sentences | Summary sentences that contain query terms.
sentences | Sentences that contain query terms.


## Barcode Recognition







```python


import requests
url="http://api.idolondemand.com/1/api/sync/recognizebarcodes/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/recognizebarcodes/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
url |
reference |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
barcode_orientation | string | Information about the barcode orientation in the images that you are submitting.
barcode_type | array | The type of barcode you are trying to recognize.

### Enums

barcode_orientation | Description
--------- | -----------
upright | Upright
any | Any


## Face Recognition







```python


import requests
url="http://api.idolondemand.com/1/api/sync/recognizefaces/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/recognizefaces/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
url |
reference |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
indexes | string | The names of one or more IOD indexes that you want to search for results.

### Enums

indexes | Description
--------- | -----------
facesinthewild | Faces in the Wild


## Image Recognition







```python


import requests
url="http://api.idolondemand.com/1/api/sync/recognizeimages/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/recognizeimages/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
image_type | string | Information about the image that you are submitting.
match_image | array | A list of unique names of images to match from the specified database.
indexes | string | The image database that contains the objects you want to recognize.

### Enums

image_type | Description
--------- | -----------
simple | Flat image, simple background
complex_3d | Skewed/distorted image, complex background
complex_2d | Flat image, complex background
indexes | Description
--------- | -----------
corporatelogos | Corporate Logos


## Speech Recognition







```python


import requests
url="http://api.idolondemand.com/1/api/sync/recognizespeech/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/recognizespeech/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
interval | number | The time interval to use to segment the speech in the output. Use -1 to turn off segmentation, 0 to segment on every word, and a positive number for a time interval (ms).
language | string | The language of the provided speech.

### Enums

language | Description
--------- | -----------
en-GB | British English
it-IT | Italian
en-US | US English
enuk | enuk
zh-CN | Mandarin
de-DE | German
fr-FR | French
enus | enus
es-ES | European Spanish


## Recommend







```python


import requests
url="http://api.idolondemand.com/1/api/sync/recommend/v1"

data=
{
"required_label":"myrequired_label",
"service_name":"myservice_name",
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/recommend/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
json |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**required_label** | string | The label required from the predictor.
**service_name** | string | The name of the service to use to activate the prediction model on data.
recommendations_amount | number | The number of recommendations to produce for every record.



## Restore Text Index







```python


import requests
url="http://api.idolondemand.com/1/api/sync/restoretextindex/v1"

data=
{
"date":"mydate",
"index":"myindex",
"new_index":"mynew_index",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/restoretextindex/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**date** | string | The date and time to restore to (in any ISO 8601 format).
**index** | string | The name of the text index to restore.
**new_index** | string | The name of the index to create with the restored data.



## Retrieve Classification







```python


import requests
url="http://api.idolondemand.com/1/api/sync/retrieveclassificationobjects/v1"

data=
{
"type":"mytype",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/retrieveclassificationobjects/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
start | number | The number of the first object to retrieve.  Default value: 1.
**type** | string | The type of classification object.
id | array | The ids of the object or objects to retrieve.
additional | object | Specify a JSON object of additional parameters relevant for the type of policy object being retrieved.
max_page_results | number | The maximum number of results to return.  If you have set the Start parameter, max_page_results sets the maximum number of results to return from the total results set. Default value: 6.

### Enums

type | Description
--------- | -----------
lexicon | Lexicon
collection | Collection
field_source | Field Source
lexicon_expression | Lexicon Expression
condition | Condition
collection_sequence | Collection Sequence


## Retrieve Config







```python


import requests
url="http://api.idolondemand.com/1/api/sync/retrieveconfig/v1"

data=
{
"connector":"myconnector",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/retrieveconfig/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**connector** | string | The name of the connector to retrieve the configuration for.
validation_key | string | Internal IOD validation key.



## Retrieve Index Fields







```python


import requests
url="http://api.idolondemand.com/1/api/sync/retrieveindexfields/v1"

data=
{
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/retrieveindexfields/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
group_fields_by_type | boolean | Set to true to group the fields by field type.
index | string | The text index from which you want to retrieve fields.
fieldtype | array | The field types for which to return field names.
max_values | number | The number of field names to display. Displays maximum 1000 tags by default.



## Retrieve Policy







```python


import requests
url="http://api.idolondemand.com/1/api/sync/retrievepolicyobjects/v1"

data=
{
"type":"mytype",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/retrievepolicyobjects/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
start | number | The number of the first object to retrieve.
**type** | string | The type of policy object to retrieve.
id | array | The ids of the policy object to retrieve.
additional | object | JSON formatted additional information depending on the object type. See the schema for more details
max_page_results | number | The maximum number of results to return. If you have set the Start parameter, max_page_results sets the maximum number of results to return from the total results set.

### Enums

type | Description
--------- | -----------
policy | Policy
policy_type | Policy Type


## Start Connector







```python


import requests
url="http://api.idolondemand.com/1/api/sync/startconnector/v1"

data=
{
"connector":"myconnector",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/startconnector/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**connector** | string | The name of the connector to start.
token | string | The token sent to your email box.
destination | object | A destination to which to the connector must send retrieved data. This value overrides the configured destination.
ignore_previous_state | boolean | Set to true to ignore the state of previous connector runs.



## Stop Connector







```python


import requests
url="http://api.idolondemand.com/1/api/sync/stopconnector/v1"

data=
{
"connector":"myconnector",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/stopconnector/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**connector** | string | The name of the connector to stop.



## Store Object







```python


import requests
url="http://api.idolondemand.com/1/api/sync/storeobject/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/storeobject/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
url |
reference |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------



## Text Tokenization







```python


import requests
url="http://api.idolondemand.com/1/api/sync/tokenizetext/v1"

data=
{
"apikey":mykey
}

#GET
data["text"]="mytext"
resp=requests.get(url,params=data)
#POST
data["text"]="mytext"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/tokenizetext/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
text |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
language | string | The language of the specified terms.
max_terms | number | The maximum number of terms to return results for.
indexes | array | The name of an IDOL OnDemand text index that you want to search for results. You can use the public datasets, or your own text indexes.
stemming | boolean | Set this parameter to false to return the list of terms in their unstemmed form.

### Enums

language | Description
--------- | -----------
ger | German
fre | French
eng | English
chi | Chinese
jap | Japanese
ita | Italian
ara | Arabic
heb | Hebrew
spa | Spanish


## Train Prediction







```python


import requests
url="http://api.idolondemand.com/1/api/sync/trainpredictor/v1"

data=
{
"service_name":"myservice_name",
"prediction_field":"myprediction_field",
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/trainpredictor/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
json |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**service_name** | string | The name of the predictor service to create. This name identifies the service and must be unique.
empty_value | string | A value to use to represent an empty value in the data set. When predicting, the API predicts categories only for occurrences of the 'prediction_field' that contain this empty value.
**prediction_field** | string | The name of the field in your data that contains the categories that you would like to predict. The prediction model is trained to fill in categories where values are missing.



## Unassign Role







```python


import requests
url="http://api.idolondemand.com/1/api/sync/unassignrole/v1"

data=
{
"role":"myrole",
"user":"myuser",
"store":"mystore",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/unassignrole/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**role** | string | The name of the role to remove from the specified user.
**user** | string | The name of the user.
**store** | string | The name of the user store.



## Update Classification







```python


import requests
url="http://api.idolondemand.com/1/api/sync/updateclassificationobjects/v1"

data=
{
"type":"mytype",
"id":"myid",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/updateclassificationobjects/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
additional | object | Specify a JSON object of additional parameters relevant for the type of classification object being updated.
description | string | A new textual description for the classification object, leave empty to remove the existing description.  Does not apply to lexicon_expression or condition types.
**type** | string | The type of classification object.
**id** | number | The id of the classification object to be updated.
name | string | The new name of the classification object.  Does not apply to lexicon_expression type.

### Enums

type | Description
--------- | -----------
lexicon | Lexicon
collection | Collection
field_source | Field Source
lexicon_expression | Lexicon Expression
condition | Condition
collection_sequence | Collection Sequence


## Update Connector







```python


import requests
url="http://api.idolondemand.com/1/api/sync/updateconnector/v1"

data=
{
"connector":"myconnector",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/updateconnector/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
description | string | A brief description of the connector.
schedule | object | A JSON string containing the details of the schedule.
destination | object | The destination to which the connector must send retrieved data. This value can be either an index or a pipeline.
credentials_license | object | The user credentials-license to verify the validity of the keys for decryption.
**connector** | string | The name of the connector to update.
credentials | object | The user credentials to use to access the source repository.
config | object | The configuration attributes, defined by attributes.json.



## Update Policy







```python


import requests
url="http://api.idolondemand.com/1/api/sync/updatepolicyobjects/v1"

data=
{
"additional":"myadditional",
"type":"mytype",
"id":"myid",
"name":"myname",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/updatepolicyobjects/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**additional** | object | Specify a JSON object of additional parameters relevant for the type of policy object being updated.
description | string | A new description for the policy object, leave empty to remove the existing description.
**type** | string | The type of policy object to update.
**id** | number | The id of the policy object to update.
**name** | string | The new name for the policy object.

### Enums

type | Description
--------- | -----------
policy | Policy
policy_type | Policy Type


## Update Query Profile







```python


import requests
url="http://api.idolondemand.com/1/api/sync/updatequeryprofile/v1"

data=
{
"query_profile":"myquery_profile",
"config":"myconfig",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/updatequeryprofile/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**query_profile** | string | The name of the query profile.
**config** | object | The content of the query profile.



## Verify







```python


import requests
url="http://api.idolondemand.com/1/api/sync/verify/v1"

data=
{
"token":"mytoken",
"apikey":mykey
}

#GET
resp=requests.get(url,params=data)
#POST
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/verify/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
**token** | string | Authentication token, as returned by the authenticate api



## View Document







```python


import requests
url="http://api.idolondemand.com/1/api/sync/viewdocument/v1"

data=
{
"apikey":mykey
}

#GET
data["url"]="myurl"
resp=requests.get(url,params=data)
#POST
data["url"]="myurl"
resp=requests.post(url,data=data)
#File POST
files={file:open("myfile.extension","rb")}
resp=requests.post(url,files=files,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/{sync|async}/viewdocument/v1`

Inputs and extra parameters should be query parameters when sending a GET request, but posted in the body when doing a POST request
Multipart-form/data POSTs are also supported and required when sending file parameters.

### Inputs

Inputs | Description
------- | -------
reference |
url |
file |


### Extra Parameters

Parameter | Type | Description
--------- | ----------- | -----------
highlight_expression | array | The terms to highlight in the document. You can also use Boolean expressions, for example, term1 AND term2.
start_tag | array | The opening HTML tag to use to highlight a link term. If specified, the number of start tags must match the number of highlight expressions.
raw_html | boolean | Set to true to output HTML suitable for direct rendering in a Web browser. Set to false to output Base 64 encoded HTML wrapped in a JSON object. The default is true.
end_tag | array | The closing HTML tag to use to highlight a link term. If omitted, this is generated automatically from the start_tag. If specified, the number of end tags must match the number of highlight expressions.



