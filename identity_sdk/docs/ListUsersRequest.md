# ListUsersRequest

Request schema for paginated and filtered listing of users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PageRequest**](PageRequest.md) |  | [optional] 
**filters** | [**UserFilters**](UserFilters.md) |  | [optional] 

## Example

```python
from identity_sdk.models.list_users_request import ListUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsersRequest from a JSON string
list_users_request_instance = ListUsersRequest.from_json(json)
# print the JSON string representation of the object
print(ListUsersRequest.to_json())

# convert the object into a dict
list_users_request_dict = list_users_request_instance.to_dict()
# create an instance of ListUsersRequest from a dict
list_users_request_from_dict = ListUsersRequest.from_dict(list_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


