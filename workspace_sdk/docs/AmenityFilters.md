# AmenityFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**status** | [**AmenityStatus**](AmenityStatus.md) |  | [optional] 

## Example

```python
from workspace_sdk.models.amenity_filters import AmenityFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AmenityFilters from a JSON string
amenity_filters_instance = AmenityFilters.from_json(json)
# print the JSON string representation of the object
print(AmenityFilters.to_json())

# convert the object into a dict
amenity_filters_dict = amenity_filters_instance.to_dict()
# create an instance of AmenityFilters from a dict
amenity_filters_from_dict = AmenityFilters.from_dict(amenity_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


