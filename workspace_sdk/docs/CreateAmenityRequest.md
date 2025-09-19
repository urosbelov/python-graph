# CreateAmenityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**type** | [**AmenityType**](AmenityType.md) |  | [optional] 

## Example

```python
from workspace_sdk.models.create_amenity_request import CreateAmenityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAmenityRequest from a JSON string
create_amenity_request_instance = CreateAmenityRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAmenityRequest.to_json())

# convert the object into a dict
create_amenity_request_dict = create_amenity_request_instance.to_dict()
# create an instance of CreateAmenityRequest from a dict
create_amenity_request_from_dict = CreateAmenityRequest.from_dict(create_amenity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


