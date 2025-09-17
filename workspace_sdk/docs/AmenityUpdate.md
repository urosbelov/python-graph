# AmenityUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**type** | [**AmenityType**](AmenityType.md) |  | [optional] 
**status** | [**AmenityStatus**](AmenityStatus.md) |  | [optional] 

## Example

```python
from workspace_sdk.models.amenity_update import AmenityUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AmenityUpdate from a JSON string
amenity_update_instance = AmenityUpdate.from_json(json)
# print the JSON string representation of the object
print(AmenityUpdate.to_json())

# convert the object into a dict
amenity_update_dict = amenity_update_instance.to_dict()
# create an instance of AmenityUpdate from a dict
amenity_update_from_dict = AmenityUpdate.from_dict(amenity_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


