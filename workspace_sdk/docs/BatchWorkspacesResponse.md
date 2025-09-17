# BatchWorkspacesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**Dict[str, WorkspaceResponse]**](WorkspaceResponse.md) |  | 

## Example

```python
from workspace_sdk.models.batch_workspaces_response import BatchWorkspacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWorkspacesResponse from a JSON string
batch_workspaces_response_instance = BatchWorkspacesResponse.from_json(json)
# print the JSON string representation of the object
print(BatchWorkspacesResponse.to_json())

# convert the object into a dict
batch_workspaces_response_dict = batch_workspaces_response_instance.to_dict()
# create an instance of BatchWorkspacesResponse from a dict
batch_workspaces_response_from_dict = BatchWorkspacesResponse.from_dict(batch_workspaces_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


