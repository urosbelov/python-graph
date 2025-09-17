# WorkspaceStatusUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**WorkspaceStatus**](WorkspaceStatus.md) |  | 

## Example

```python
from workspace_sdk.models.workspace_status_update import WorkspaceStatusUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceStatusUpdate from a JSON string
workspace_status_update_instance = WorkspaceStatusUpdate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceStatusUpdate.to_json())

# convert the object into a dict
workspace_status_update_dict = workspace_status_update_instance.to_dict()
# create an instance of WorkspaceStatusUpdate from a dict
workspace_status_update_from_dict = WorkspaceStatusUpdate.from_dict(workspace_status_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


