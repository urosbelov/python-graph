# ListAmenitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**AmenityFilters**](AmenityFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 

## Example

```python
from workspace_sdk.models.list_amenities_request import ListAmenitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListAmenitiesRequest from a JSON string
list_amenities_request_instance = ListAmenitiesRequest.from_json(json)
# print the JSON string representation of the object
print(ListAmenitiesRequest.to_json())

# convert the object into a dict
list_amenities_request_dict = list_amenities_request_instance.to_dict()
# create an instance of ListAmenitiesRequest from a dict
list_amenities_request_from_dict = ListAmenitiesRequest.from_dict(list_amenities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


