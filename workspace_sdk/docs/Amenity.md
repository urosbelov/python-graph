# Amenity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | [**AmenityStatus**](AmenityStatus.md) |  | [optional] 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deprecated_at** | **datetime** |  | [optional] 
**deprecated_by** | **str** |  | [optional] 
**type** | [**AmenityType**](AmenityType.md) |  | [optional] 
**name** | **str** |  | 
**key** | **str** |  | 
**icon** | **str** |  | [optional] 

## Example

```python
from workspace_sdk.models.amenity import Amenity

# TODO update the JSON string below
json = "{}"
# create an instance of Amenity from a JSON string
amenity_instance = Amenity.from_json(json)
# print the JSON string representation of the object
print(Amenity.to_json())

# convert the object into a dict
amenity_dict = amenity_instance.to_dict()
# create an instance of Amenity from a dict
amenity_from_dict = Amenity.from_dict(amenity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


