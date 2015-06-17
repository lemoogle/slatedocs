

# Posting files

Many APIs require files to be posted to the API. For these APIs or file inputs, a Multipart-form/data post call is required.

The APIs that you will likely want to use file posts with are


```shell

#Sending a scanned pdf to the OCR API

curl -X POST --form "apikey=<API_KEY>" --form "file=@myscan.pdf" --form "mode=document_photo" https://api.idolondemand.com/1/api/async/ocrdocument/v1

```

```python
files = {'file': open('myscan.pdf', 'rb')}
data= {'apikey':myapikey,'mode':'document_photo'}
requests.post("https://api.idolondemand.com/1/api/async/ocrdocument/v1",data=data,files=files)
print r.json()
```

```javascript
var needle = require('needle');
var data = {
  apikey: myapikey,
  file: { file: 'myscan.pdf', content_type: 'multipart/form-data' }
}

needle.post('https://api.idolondemand.com/1/api/async/ocrdocument/v1', data, { multipart: true }, function(err, resp, body) {
  console.log(body)
  // needle will read the file and include it in the form-data as binary
});
```
