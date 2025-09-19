# GetUsersBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | 

## Example

```python
from identity_sdk.models.get_users_batch_request import GetUsersBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersBatchRequest from a JSON string
get_users_batch_request_instance = GetUsersBatchRequest.from_json(json)
# print the JSON string representation of the object
print(GetUsersBatchRequest.to_json())

# convert the object into a dict
get_users_batch_request_dict = get_users_batch_request_instance.to_dict()
# create an instance of GetUsersBatchRequest from a dict
get_users_batch_request_from_dict = GetUsersBatchRequest.from_dict(get_users_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


