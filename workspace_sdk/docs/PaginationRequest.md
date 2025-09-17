# PaginationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**cursor** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 

## Example

```python
from workspace_sdk.models.pagination_request import PaginationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequest from a JSON string
pagination_request_instance = PaginationRequest.from_json(json)
# print the JSON string representation of the object
print(PaginationRequest.to_json())

# convert the object into a dict
pagination_request_dict = pagination_request_instance.to_dict()
# create an instance of PaginationRequest from a dict
pagination_request_from_dict = PaginationRequest.from_dict(pagination_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


