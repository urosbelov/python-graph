# BatchWorkspacesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 

## Example

```python
from workspace_sdk.models.batch_workspaces_request import BatchWorkspacesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWorkspacesRequest from a JSON string
batch_workspaces_request_instance = BatchWorkspacesRequest.from_json(json)
# print the JSON string representation of the object
print(BatchWorkspacesRequest.to_json())

# convert the object into a dict
batch_workspaces_request_dict = batch_workspaces_request_instance.to_dict()
# create an instance of BatchWorkspacesRequest from a dict
batch_workspaces_request_from_dict = BatchWorkspacesRequest.from_dict(batch_workspaces_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


