# Client Libraries

## Ruby

###[iodruby](https://github.com/HP-IDOL-OnDemand/iodruby)
A small ruby library to call IDOL OnDemand APIs.



```ruby
require "iodruby"
client= IODClient.new("http://api.idolondemand.com",$apikey)
r=client.post('analyzesentiment',{:text=>'I like cats'})
```

## Python

###[iod-python](https://github.com/HP-IDOL-OnDemand/iod-python)
A small python library to call IDOL OnDemand APIs.

```python
from iodpython.iodindex import IODClient
client = IODClient("http://api.idolondemand.com/",
                            "myapikey")
r=client.post(handler,{'param1':'value1','param2':'value2'})
r=client.post('analyzesentiment',{'text':'I like cats'})

```

## Node.js

```javascript
//idol-client
var MyClient = require('idol-client')('MyRegisteredAPIkey');
var MyClient = IDOLclient('MyRegisteredAPIkey')

//index status API
MyClient.indexStatus({
    parameters: {
        index: 'myIndexName'
    }
}).then(
    function(res){
        console.log(res.code);    // => 200-299
        console.log(res.headers);    // => Response headers
        console.log(res.data);    // => Response data
    },
    function(error){ console.log('Ups, some error occured:', error); }
);
```
>---------------

```javascript
//iod-node
var iod = require('iod-node')
client= new iod.IODClient('http://api.idolondemand.com','apikey')

var callback = function(err,resp,body){
  console.log(body)
}
var data= {'text':'I like cats'}
client.call('analyzesentiment',callback,data)
```

###[idol-client](https://github.com/ColorfullyMe/idol-client)
Javascript client for working with the HP's IDOL OnDemand API from Node.js and the browser.


###[iod-node](https://github.com/HP-IDOL-OnDemand/iod-node)
A small nodejs library to call IDOL OnDemand APIs.



## Java

[Java IOD CLient](https://github.com/hpautonomy/java-iod-client) - A quick java library that some of our dev teams use when working with IOD.

```java
final RestAdapter restAdapter = new RestAdapter.Builder()
    .setEndpoint("https://api.idolondemand.com/1")
    .setConverter(new IodConverter(new JacksonConverter()))
    .setErrorHandler(new IodErrorHandler())
    .build();

final QueryTextIndexService queryTextIndexService = restAdapter.create(QueryTextIndexService.class);

final Map<String, Object> params = new QueryTextIndexRequestBuilder()
    .setAbsoluteMaxResults(10)
    .setTotalResults(true)
    .setIndexes("wiki_eng")
    .build();

final Documents documents = queryTextIndexService.queryTextIndexWithText(
    "myApiKey",
    "cats",
    params);
```


Java

Ruby

iodruby - A small ruby library to call IDOL OnDemand APIs.

Javascript

idol-client - Javascript client for working with the HP's IDOL OnDemand API from Node.js and the browser.

iod-node - A small nodejs library to call IDOL OnDemand APIs.

Python

iod-python - A small python library to call IDOL OnDemand APIs.
