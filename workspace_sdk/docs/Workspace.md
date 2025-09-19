# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**base62_id** | **str** |  | 
**status** | [**WorkspaceStatus**](WorkspaceStatus.md) |  | [optional] 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**deleted_by** | **str** |  | [optional] 
**type** | [**WorkspaceType**](WorkspaceType.md) |  | [optional] 
**name** | **str** |  | 
**handle** | **str** |  | 
**description** | **str** |  | [optional] 
**category_id** | **int** |  | 
**formatted_address** | **str** |  | [optional] 
**avatar_id** | **str** |  | [optional] 
**cover_id** | **str** |  | [optional] 
**location** | [**Point**](Point.md) |  | [optional] 

## Example

```python
from workspace_sdk.models.workspace import Workspace

# TODO update the JSON string below
json = "{}"
# create an instance of Workspace from a JSON string
workspace_instance = Workspace.from_json(json)
# print the JSON string representation of the object
print(Workspace.to_json())

# convert the object into a dict
workspace_dict = workspace_instance.to_dict()
# create an instance of Workspace from a dict
workspace_from_dict = Workspace.from_dict(workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


