

# Asynchronous and Synchronous calls

API calls are in the form `http://idolondemand.com/api/1/{sync,async}/{apiname}/v1`

The sync/async part of the url can be used to differentiate between a synchronous and an asynchronous call.

An **Asynchronous** call will return a jobID, that jobID can then be polled for a result, this is recommended for API calls that will take long. It is the only mode alowed for the [Recognize Speech API]()

Let's consider a sentiment analysis example

## Synchronous

```shell
curl `http://api.idolondemand.com/1/api/sync/analyzesentiment/v1?text=I%20like%20cats&apikey=apikey`
```
> The above command returns JSON structured like this:

```json
{
...
  "aggregate": {
    "sentiment": "positive",
    "score": 0.7176687736973063
  }
}
```

### HTTP Request

`GET http://api.idolondemand.com/1/api/sync/{handler}/v1`

## Asynchronous

```shell
curl http://api.idolondemand.com/1/api/async/analyzesentiment/v1?text=I%20like%20cats&apikey=apikey
```
> The above command returns JSON structured like this:

```json
{
"jobID": "usw3p_3eb5f2a4-3950-4f67-ab58-6597e9fe17ca"
}
```

```shell

curl https://api.idolondemand.com/1/job/status/usw3p_3eb5f2a4-3950-4f67-ab58-6597e9fe17ca?apikey=myapikey
```

```json
{
  "actions": [{
    "result": {
      "positive": [{
        "sentiment": "like",
        "topic": "cats",
        "score": 0.7176687736973063,
        "original_text": "I like cats",
        "original_length": 11,
        "normalized_text": "I like cats",
        "normalized_length": 11
      }],
      "negative": [],
      "aggregate": {
        "sentiment": "positive",
        "score": 0.7176687736973063
      }
    },
    "status": "finished",
    "action": "analyzesentiment",
    "version": "v1"
  }],
  "jobID": "usw3p_3eb5f2a4-3950-4f67-ab58-6597e9fe17ca",
  "status": "finished"
}
```

### Job Status - HTTP Request

`GET https://api.idolondemand.com/1/job/status/jobid?apikey=myapikey`

This call will poll the jobid for a status. If the status is **Finished** the result will be returned as well.

### Job Result - HTTP Request

`GET https://api.idolondemand.com/1/job/result/jobid?apikey=myapikey`

Sometimes you want to send one call and wait until the result is ready, this is the same as sending a synchronous call. *Not recommended for production when expecting long calls as this may time out*
