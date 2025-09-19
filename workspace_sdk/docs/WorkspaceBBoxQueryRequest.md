# WorkspaceBBoxQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**BBox**](BBox.md) |  | 
**filters** | [**WorkspaceBBoxFilters**](WorkspaceBBoxFilters.md) |  | [optional] 

## Example

```python
from workspace_sdk.models.workspace_b_box_query_request import WorkspaceBBoxQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceBBoxQueryRequest from a JSON string
workspace_b_box_query_request_instance = WorkspaceBBoxQueryRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceBBoxQueryRequest.to_json())

# convert the object into a dict
workspace_b_box_query_request_dict = workspace_b_box_query_request_instance.to_dict()
# create an instance of WorkspaceBBoxQueryRequest from a dict
workspace_b_box_query_request_from_dict = WorkspaceBBoxQueryRequest.from_dict(workspace_b_box_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


