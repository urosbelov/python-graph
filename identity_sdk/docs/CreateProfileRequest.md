# CreateProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** |  | 
**device_id** | **str** |  | 
**profile** | [**UserCreateProfile**](UserCreateProfile.md) |  | 

## Example

```python
from identity_sdk.models.create_profile_request import CreateProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProfileRequest from a JSON string
create_profile_request_instance = CreateProfileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProfileRequest.to_json())

# convert the object into a dict
create_profile_request_dict = create_profile_request_instance.to_dict()
# create an instance of CreateProfileRequest from a dict
create_profile_request_from_dict = CreateProfileRequest.from_dict(create_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


