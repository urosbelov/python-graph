# WorkspaceBBoxFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**WorkspaceStatus**](WorkspaceStatus.md) |  | [optional] 
**category_ids** | **List[int]** |  | [optional] 

## Example

```python
from workspace_sdk.models.workspace_b_box_filters import WorkspaceBBoxFilters

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceBBoxFilters from a JSON string
workspace_b_box_filters_instance = WorkspaceBBoxFilters.from_json(json)
# print the JSON string representation of the object
print(WorkspaceBBoxFilters.to_json())

# convert the object into a dict
workspace_b_box_filters_dict = workspace_b_box_filters_instance.to_dict()
# create an instance of WorkspaceBBoxFilters from a dict
workspace_b_box_filters_from_dict = WorkspaceBBoxFilters.from_dict(workspace_b_box_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


