# WorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**key** | **str** |  | 
**type** | [**WorkspaceType**](WorkspaceType.md) |  | [optional] 
**status** | [**WorkspaceStatus**](WorkspaceStatus.md) |  | [optional] 
**name** | **str** |  | 
**handle** | **str** |  | 
**category_id** | **int** |  | 
**avatar_id** | **str** |  | [optional] 
**cover_id** | **str** |  | [optional] 
**formatted_address** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**deleted_by** | **str** |  | [optional] 

## Example

```python
from workspace_sdk.models.workspace_response import WorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceResponse from a JSON string
workspace_response_instance = WorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceResponse.to_json())

# convert the object into a dict
workspace_response_dict = workspace_response_instance.to_dict()
# create an instance of WorkspaceResponse from a dict
workspace_response_from_dict = WorkspaceResponse.from_dict(workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


