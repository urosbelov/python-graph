# UserFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**status** | [**UserStatus**](UserStatus.md) |  | [optional] 

## Example

```python
from identity_sdk.models.user_filters import UserFilters

# TODO update the JSON string below
json = "{}"
# create an instance of UserFilters from a JSON string
user_filters_instance = UserFilters.from_json(json)
# print the JSON string representation of the object
print(UserFilters.to_json())

# convert the object into a dict
user_filters_dict = user_filters_instance.to_dict()
# create an instance of UserFilters from a dict
user_filters_from_dict = UserFilters.from_dict(user_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


