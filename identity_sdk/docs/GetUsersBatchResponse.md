# GetUsersBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**Dict[str, UserResponse]**](UserResponse.md) |  | 

## Example

```python
from identity_sdk.models.get_users_batch_response import GetUsersBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersBatchResponse from a JSON string
get_users_batch_response_instance = GetUsersBatchResponse.from_json(json)
# print the JSON string representation of the object
print(GetUsersBatchResponse.to_json())

# convert the object into a dict
get_users_batch_response_dict = get_users_batch_response_instance.to_dict()
# create an instance of GetUsersBatchResponse from a dict
get_users_batch_response_from_dict = GetUsersBatchResponse.from_dict(get_users_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


