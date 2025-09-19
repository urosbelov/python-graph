# GetFeaturesBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**Dict[str, Feature]**](Feature.md) |  | 

## Example

```python
from workspace_sdk.models.get_features_batch_response import GetFeaturesBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeaturesBatchResponse from a JSON string
get_features_batch_response_instance = GetFeaturesBatchResponse.from_json(json)
# print the JSON string representation of the object
print(GetFeaturesBatchResponse.to_json())

# convert the object into a dict
get_features_batch_response_dict = get_features_batch_response_instance.to_dict()
# create an instance of GetFeaturesBatchResponse from a dict
get_features_batch_response_from_dict = GetFeaturesBatchResponse.from_dict(get_features_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


