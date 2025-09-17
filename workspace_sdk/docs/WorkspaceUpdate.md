# WorkspaceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WorkspaceType**](WorkspaceType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**avatar_id** | **str** |  | [optional] 
**cover_id** | **str** |  | [optional] 
**formatted_address** | **str** |  | [optional] 

## Example

```python
from workspace_sdk.models.workspace_update import WorkspaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUpdate from a JSON string
workspace_update_instance = WorkspaceUpdate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUpdate.to_json())

# convert the object into a dict
workspace_update_dict = workspace_update_instance.to_dict()
# create an instance of WorkspaceUpdate from a dict
workspace_update_from_dict = WorkspaceUpdate.from_dict(workspace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


