# WorkspaceFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**WorkspaceStatus**](WorkspaceStatus.md) |  | [optional] 
**name** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_after** | **datetime** |  | [optional] 
**created_before** | **datetime** |  | [optional] 
**google_place_id** | **str** |  | [optional] 
**bbox** | [**BBox**](BBox.md) |  | [optional] 
**radius_m** | **int** |  | [optional] 
**location** | [**LatLng**](LatLng.md) |  | [optional] 

## Example

```python
from workspace_sdk.models.workspace_filters import WorkspaceFilters

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceFilters from a JSON string
workspace_filters_instance = WorkspaceFilters.from_json(json)
# print the JSON string representation of the object
print(WorkspaceFilters.to_json())

# convert the object into a dict
workspace_filters_dict = workspace_filters_instance.to_dict()
# create an instance of WorkspaceFilters from a dict
workspace_filters_from_dict = WorkspaceFilters.from_dict(workspace_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


