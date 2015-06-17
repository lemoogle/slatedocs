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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/addagent/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/addrole/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/addstore/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/addtotextindex/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/adduser/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/analyzesentiment/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/assignrole/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/authenticate/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/cancelconnectorschedule/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/categorizedocument/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/classifydocument/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/connectorhistory/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/connectorstatus/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/createclassificationobjects/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/createconnector/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/createpolicyobjects/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/createqueryprofile/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/createtextindex/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deleteagent/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deleteclassificationobjects/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deleteconnector/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deletefromtextindex/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deletepolicyobjects/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deletequeryprofile/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deleterole/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deletestore/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deletetextindex/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/deleteuser/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/detectfaces/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/expandcontainer/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/expandterms/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/extractconcepts/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/extractentities/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/extracttext/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/findrelatedconcepts/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/findsimilar/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/getcontent/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/getparametricvalues/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/highlighttext/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/identifylanguage/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/indexstatus/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/listagents/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/listindexes/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/listresources/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/listroles/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/liststores/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/listuserroles/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/listusers/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/ocrdocument/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/predict/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/querytextindex/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/recognizebarcodes/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/recognizefaces/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/recognizeimages/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/recognizespeech/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/recommend/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/restoretextindex/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/retrieveclassificationobjects/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/retrieveconfig/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/retrieveindexfields/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/retrievepolicyobjects/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/startconnector/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/stopconnector/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/storeobject/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/tokenizetext/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/trainpredictor/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/unassignrole/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/updateclassificationobjects/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/updateconnector/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/updatepolicyobjects/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/updatequeryprofile/{sync|async}`

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
data[""]="my"
resp=requests.get(url,params=data)
#POST
data[""]="my"
resp=requests.post(url,data=data)
```



### HTTP Request

`GET/POST http://api.idolondemand.com/1/api/verify/{sync|async}`

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

`GET/POST http://api.idolondemand.com/1/api/viewdocument/{sync|async}`

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
