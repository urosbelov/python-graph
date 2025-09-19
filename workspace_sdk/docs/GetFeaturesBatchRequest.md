# GetFeaturesBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_ids** | **List[str]** |  | 

## Example

```python
from workspace_sdk.models.get_features_batch_request import GetFeaturesBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeaturesBatchRequest from a JSON string
get_features_batch_request_instance = GetFeaturesBatchRequest.from_json(json)
# print the JSON string representation of the object
print(GetFeaturesBatchRequest.to_json())

# convert the object into a dict
get_features_batch_request_dict = get_features_batch_request_instance.to_dict()
# create an instance of GetFeaturesBatchRequest from a dict
get_features_batch_request_from_dict = GetFeaturesBatchRequest.from_dict(get_features_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


