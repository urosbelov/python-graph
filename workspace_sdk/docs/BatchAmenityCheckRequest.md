# BatchAmenityCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**amenity_ids** | **List[int]** |  | 

## Example

```python
from workspace_sdk.models.batch_amenity_check_request import BatchAmenityCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAmenityCheckRequest from a JSON string
batch_amenity_check_request_instance = BatchAmenityCheckRequest.from_json(json)
# print the JSON string representation of the object
print(BatchAmenityCheckRequest.to_json())

# convert the object into a dict
batch_amenity_check_request_dict = batch_amenity_check_request_instance.to_dict()
# create an instance of BatchAmenityCheckRequest from a dict
batch_amenity_check_request_from_dict = BatchAmenityCheckRequest.from_dict(batch_amenity_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


