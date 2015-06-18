#Errors


The IDOL OnDemand API uses the following error codes.

Error Code | Description | HTTP Response Code
---- | --- | ---
1000 | Unknown | 500

##Status Codes

These messages indicate a status rather than an error.

Error Code | Description | HTTP Response Code
---- | --- | ---
1001 | Queued | 200
1002 | In Progress | 200
1003 | Failed | 200
1004 | Unknown Status | 500

##API Key Errors

For more information about creating and administering API keys, see API Keys.

Error Code | Description | HTTP Response Code
---- | --- | ---
2000 | API key required | 401
2001 | Invalid API key | 400
2002 | Unknown API key | 401
2003 | The given API key is not authorized | 403
2004 | User account is disabled | 403

##Quota Errors

These errors apply for quotas. For more information about quotas and rate limiting, see Rate limiting, Quotas, Data Expiry, and Maximums.

Error Code | Description | HTTP Response Code
---- | --- | ---
2010 | A quota has been violated, see additional details | 400
2020 | Cannot get quota info for invalid quota | 400

##Job ID Errors

These errors apply to asynchronous actions. For more information about the asynchronous API, see Synchronous and Asynchronous API.

Error Code | Description | HTTP Response Code
---- | --- | ---
3000 | Missing job ID | 400
3001 | Invalid job ID | 400
3002 | Cannot complete job | 500

##General API Call Errors

These errors occur when there is a problem with your input values. See the API documentation.

Error Code | Description | HTTP Response Code
---- | --- | ---
4000 | Duplicate parameters | 400
4001 | No file submitted | 400
4002 | No job actions submitted | 400
4003 | Invalid job actions | 400
4004 | Invalid job action | 400
4005 | Invalid job action parameters | 400
4006 | Invalid job action parameter | 400
4007 | Invalid job action parameter name | 400
4008 | Invalid job action parameter value | 400
4009 | Missing job action name | 400
4010 | Invalid JSON submitted | 400
4011 | File UUID does not exist | 400
4012 | File UUID refers to a non-existent file | 400
4013 | HTTP GET request failed | 400
4014 | Invalid URL | 400
4015 | Missing required parameter(s) | 400
4016 | Missing job action version | 400
4017 | HTTP GET request did not complete in time | 400
4018 | HTTP GET request had too many redirects | 400
4019 | HTTP GET request timed out before the server responded | 400
4020 | Invalid query text | 400
4021 | Invalid field name | 400
4022 | Action not processed | 400
4023 | Invalid field value | 400
4024 | Field_text contains operation on unoptimized fields | 400
4025 | The text sent as input is too long | 400
4026 | Invalid value for an array parameter | 400
4027 | Failed to parse URL | 400
Project Quota Errors
4030 | Too many requests for this project | 429
Backend Errors
Note: If a backend error persists, please raise a support ticket.
5000 | Backend request failed | 500
5001 | A previous job action failed | 500
5002 | Could not process job | 500
5003 | Job result was invalid | 500
5004 | Could not process job | 500
5005 | Job expired before reaching the worker | 500
5006 | Fatal database error | 500
5007 | Job took too long to process | 500
5008 | Key Management Service Error | 400
5009 | Key Management Service Initialization Error | 400

##File Errors

Error Code | Description | HTTP Response Code
---- | --- | ---
5010 | File is password protected | 400
5011 | Invalid file format | 400
5012 | Unknown file format | 400
5013 | Reference does not exist | 400

##Specific API Call Errors

The following errors apply only to a particular API or a set of APIs.

Error Code | Description | HTTP Response Code
---- | --- | ---
5020 | No valid documents were given | 400
5021 | Some documents that were given are invalid | 400
5030 | Invalid value for 'expansion'. This error applies to the Expand Terms API. | 400
5040 | Invalid value for 'language' | 400
5050 | Invalid value for 'entitytype'. This error applies to the Entity Extraction API. | 400
5060 | Invalid image file. This error applies to the Image Analysis APIs. | 400
5070 | 'highlightexpression' and 'starttag' are mismatched. This error applies to the View Document API. | 400
5080 | Invalid 'confirm' token. This error applies to the Delete From Text Index API. | 400
5090 | 'match_image' refers to a missing object. This error applies to the Image Recognition API. | 400

##Page Errors
Error Code | Description | HTTP Response Code
---- | --- | ---
6000 | Page not found | 404

##Request Size Errors

Error Code | Description | HTTP Response Code
---- | --- | ---
7000 | Request took too long | 504
7001 | Too many fields in the request | 413
7002 | URL encoded request was too long. Try sending a multipart request. | 413
7003 | Multipart request contained a field that was too long. Send long text as files. | 413
7004 | Too many files attached to request | 413
7005 | Invalid POST request received | 400
7006 | Multipart request too big | 413
7007 | Client closed socket | 418
7008 | An unknown error closed the socket | 418
7009 | Unsupported request method | 405

##Text Index Errors

Error Code | Description | HTTP Response Code
---- | --- | ---
8001 | Content full | 400
8002 | Index name invalid | 400
8004 | Connector name invalid | 400
8005 | Index component already has an available instance | 400
8006 | The operation is unsupported for the given index because it is too old | 400

##Index Quota Errors

Error Code | Description | HTTP Response Code
---- | --- | ---
9000 | Reached index quota | 400
9001 | Index is full | 400
9002 | Reached field count quota | 400

##Connector Quota Errors

Error Code | Description | HTTP Response Code
---- | --- | ---
9003 | Reached connector count quota | 400
9004 | Reached start connector quota | 400
9005 | Reached the minimum connector schedule interval quota | 400
9006 | Reached the maximum runs quota for 24 hour interval | 400

##Job Errors

Error Code | Description | HTTP Response Code
---- | --- | ---
10000 | Previous job is already in progress | 429
10001 | Rejected because some jobs have been taking longer than expected | 429
10002 | Reference to a deleted database was found | 429
10003 | Invalid parameter(s) | 400

User Management Errors

Error Code | Description | HTTP Response Code
---- | --- | ---
11000 | Store not found | 400
11001 | User not found | 400
11002 | Store name already used | 400
11003 | Email address already used | 400
11004 | User Management action failed | 500
11005 | Agent name already used | 400
11006 | Agent not found | 400
11007 | Role name already used | 400
11008 | Role not found | 400
11013 | Error parsing Boolean expression | 400

Query Manipulation Errors

Error Code | Description | HTTP Response Code
---- | --- | ---
12001 | Query profile name invalid | 400
12002 | Query profile name not provided | 400
12003 | Query manipulation index invalid | 400
12004 | Query manipulation index missing | 400
