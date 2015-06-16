# Authentication

> To authorize, use this code:

```ruby
require 'IDOL OnDemand'

api = IDOL OnDemand::APIClient.authorize!('meowmeowmeow')
```

```python
import IDOL OnDemand

api = IDOL OnDemand.authorize('meowmeowmeow')
```

```shell

# With shell, you can just pass the correct header with each request

curl "http://idolondemand.com/api/1/{sync,async}/{apiname}/v1?apikey=mykey!"

curl -X POST "http://idolondemand.com/api/1/{sync,async}/{apiname}/v1"
-d "apikey=mykey!"
```

> Make sure to replace `mykey!` with your API key.

IDOL OnDemand uses API keys to allow access to the API. You can register a new IDOL OnDemand API key at our [developer portal](http://idolondemand.com).

Once you are signed up and ready to go, head to your [account page](https://www.idolondemand.com/account/api-keys.html) ( Tools -> Account -> Manage API keys ) to get your key.


IDOL OnDemand expects for the API key to be included in all API requests to the server in a get or post parameter (depending on the call method) that looks like the following:

`apikey=mykey!`

<aside class="notice">
You must replace `mykey!` with your personal API key.
</aside>
