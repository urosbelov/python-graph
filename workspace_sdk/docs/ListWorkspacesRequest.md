# ListWorkspacesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PageRequest**](PageRequest.md) |  | [optional] 
**filters** | [**WorkspaceFilters**](WorkspaceFilters.md) |  | [optional] 

## Example

```python
from workspace_sdk.models.list_workspaces_request import ListWorkspacesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkspacesRequest from a JSON string
list_workspaces_request_instance = ListWorkspacesRequest.from_json(json)
# print the JSON string representation of the object
print(ListWorkspacesRequest.to_json())

# convert the object into a dict
list_workspaces_request_dict = list_workspaces_request_instance.to_dict()
# create an instance of ListWorkspacesRequest from a dict
list_workspaces_request_from_dict = ListWorkspacesRequest.from_dict(list_workspaces_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


