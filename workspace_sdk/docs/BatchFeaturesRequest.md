# BatchFeaturesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_ids** | **List[int]** |  | 

## Example

```python
from workspace_sdk.models.batch_features_request import BatchFeaturesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchFeaturesRequest from a JSON string
batch_features_request_instance = BatchFeaturesRequest.from_json(json)
# print the JSON string representation of the object
print(BatchFeaturesRequest.to_json())

# convert the object into a dict
batch_features_request_dict = batch_features_request_instance.to_dict()
# create an instance of BatchFeaturesRequest from a dict
batch_features_request_from_dict = BatchFeaturesRequest.from_dict(batch_features_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


