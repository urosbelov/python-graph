# AuthenticatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserResponse**](UserResponse.md) |  | 
**session** | [**SessionResponse**](SessionResponse.md) |  | 

## Example

```python
from identity_sdk.models.authenticated_response import AuthenticatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedResponse from a JSON string
authenticated_response_instance = AuthenticatedResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedResponse.to_json())

# convert the object into a dict
authenticated_response_dict = authenticated_response_instance.to_dict()
# create an instance of AuthenticatedResponse from a dict
authenticated_response_from_dict = AuthenticatedResponse.from_dict(authenticated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


