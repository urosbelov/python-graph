# GetAmenitiesBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenity_ids** | **List[int]** |  | 

## Example

```python
from workspace_sdk.models.get_amenities_batch_request import GetAmenitiesBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAmenitiesBatchRequest from a JSON string
get_amenities_batch_request_instance = GetAmenitiesBatchRequest.from_json(json)
# print the JSON string representation of the object
print(GetAmenitiesBatchRequest.to_json())

# convert the object into a dict
get_amenities_batch_request_dict = get_amenities_batch_request_instance.to_dict()
# create an instance of GetAmenitiesBatchRequest from a dict
get_amenities_batch_request_from_dict = GetAmenitiesBatchRequest.from_dict(get_amenities_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


