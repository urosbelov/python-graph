# BatchAmenitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 

## Example

```python
from workspace_sdk.models.batch_amenities_request import BatchAmenitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAmenitiesRequest from a JSON string
batch_amenities_request_instance = BatchAmenitiesRequest.from_json(json)
# print the JSON string representation of the object
print(BatchAmenitiesRequest.to_json())

# convert the object into a dict
batch_amenities_request_dict = batch_amenities_request_instance.to_dict()
# create an instance of BatchAmenitiesRequest from a dict
batch_amenities_request_from_dict = BatchAmenitiesRequest.from_dict(batch_amenities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


