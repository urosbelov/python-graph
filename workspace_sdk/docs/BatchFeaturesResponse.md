# BatchFeaturesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **Dict[str, List[FeatureResponse]]** |  | 

## Example

```python
from workspace_sdk.models.batch_features_response import BatchFeaturesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchFeaturesResponse from a JSON string
batch_features_response_instance = BatchFeaturesResponse.from_json(json)
# print the JSON string representation of the object
print(BatchFeaturesResponse.to_json())

# convert the object into a dict
batch_features_response_dict = batch_features_response_instance.to_dict()
# create an instance of BatchFeaturesResponse from a dict
batch_features_response_from_dict = BatchFeaturesResponse.from_dict(batch_features_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


