# UpdateWorkspaceRequest


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
from workspace_sdk.models.update_workspace_request import UpdateWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspaceRequest from a JSON string
update_workspace_request_instance = UpdateWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkspaceRequest.to_json())

# convert the object into a dict
update_workspace_request_dict = update_workspace_request_instance.to_dict()
# create an instance of UpdateWorkspaceRequest from a dict
update_workspace_request_from_dict = UpdateWorkspaceRequest.from_dict(update_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


