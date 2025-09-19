# UserCreateProfile

Input schema for creating a user profile (includes password)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**birthday** | **datetime** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from identity_sdk.models.user_create_profile import UserCreateProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateProfile from a JSON string
user_create_profile_instance = UserCreateProfile.from_json(json)
# print the JSON string representation of the object
print(UserCreateProfile.to_json())

# convert the object into a dict
user_create_profile_dict = user_create_profile_instance.to_dict()
# create an instance of UserCreateProfile from a dict
user_create_profile_from_dict = UserCreateProfile.from_dict(user_create_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


