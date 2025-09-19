# GetAmenitiesBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | [**Dict[str, Amenity]**](Amenity.md) |  | 

## Example

```python
from workspace_sdk.models.get_amenities_batch_response import GetAmenitiesBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAmenitiesBatchResponse from a JSON string
get_amenities_batch_response_instance = GetAmenitiesBatchResponse.from_json(json)
# print the JSON string representation of the object
print(GetAmenitiesBatchResponse.to_json())

# convert the object into a dict
get_amenities_batch_response_dict = get_amenities_batch_response_instance.to_dict()
# create an instance of GetAmenitiesBatchResponse from a dict
get_amenities_batch_response_from_dict = GetAmenitiesBatchResponse.from_dict(get_amenities_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


