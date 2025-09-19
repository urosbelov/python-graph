# UserCreateAdminRequest

Input schema for creating a user by admin (no password)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 
**identifier_type** | [**IdentifierType**](IdentifierType.md) |  | 
**identifier_value** | **str** |  | 

## Example

```python
from identity_sdk.models.user_create_admin_request import UserCreateAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateAdminRequest from a JSON string
user_create_admin_request_instance = UserCreateAdminRequest.from_json(json)
# print the JSON string representation of the object
print(UserCreateAdminRequest.to_json())

# convert the object into a dict
user_create_admin_request_dict = user_create_admin_request_instance.to_dict()
# create an instance of UserCreateAdminRequest from a dict
user_create_admin_request_from_dict = UserCreateAdminRequest.from_dict(user_create_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


