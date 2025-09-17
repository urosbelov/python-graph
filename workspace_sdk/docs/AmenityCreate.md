# AmenityCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**AmenityType**](AmenityType.md) |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from workspace_sdk.models.amenity_create import AmenityCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AmenityCreate from a JSON string
amenity_create_instance = AmenityCreate.from_json(json)
# print the JSON string representation of the object
print(AmenityCreate.to_json())

# convert the object into a dict
amenity_create_dict = amenity_create_instance.to_dict()
# create an instance of AmenityCreate from a dict
amenity_create_from_dict = AmenityCreate.from_dict(amenity_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


