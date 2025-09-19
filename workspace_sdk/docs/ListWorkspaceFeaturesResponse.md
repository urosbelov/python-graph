# ListWorkspaceFeaturesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Feature]**](Feature.md) |  | 

## Example

```python
from workspace_sdk.models.list_workspace_features_response import ListWorkspaceFeaturesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkspaceFeaturesResponse from a JSON string
list_workspace_features_response_instance = ListWorkspaceFeaturesResponse.from_json(json)
# print the JSON string representation of the object
print(ListWorkspaceFeaturesResponse.to_json())

# convert the object into a dict
list_workspace_features_response_dict = list_workspace_features_response_instance.to_dict()
# create an instance of ListWorkspaceFeaturesResponse from a dict
list_workspace_features_response_from_dict = ListWorkspaceFeaturesResponse.from_dict(list_workspace_features_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


