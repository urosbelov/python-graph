# GetWorkspacesBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 

## Example

```python
from workspace_sdk.models.get_workspaces_batch_request import GetWorkspacesBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkspacesBatchRequest from a JSON string
get_workspaces_batch_request_instance = GetWorkspacesBatchRequest.from_json(json)
# print the JSON string representation of the object
print(GetWorkspacesBatchRequest.to_json())

# convert the object into a dict
get_workspaces_batch_request_dict = get_workspaces_batch_request_instance.to_dict()
# create an instance of GetWorkspacesBatchRequest from a dict
get_workspaces_batch_request_from_dict = GetWorkspacesBatchRequest.from_dict(get_workspaces_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


