# ListAmenitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Amenity]**](Amenity.md) |  | 
**pagination** | [**PageResponse**](PageResponse.md) |  | 

## Example

```python
from workspace_sdk.models.list_amenities_response import ListAmenitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAmenitiesResponse from a JSON string
list_amenities_response_instance = ListAmenitiesResponse.from_json(json)
# print the JSON string representation of the object
print(ListAmenitiesResponse.to_json())

# convert the object into a dict
list_amenities_response_dict = list_amenities_response_instance.to_dict()
# create an instance of ListAmenitiesResponse from a dict
list_amenities_response_from_dict = ListAmenitiesResponse.from_dict(list_amenities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


