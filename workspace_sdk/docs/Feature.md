# Feature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | [**FeatureStatus**](FeatureStatus.md) |  | [optional] 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**deleted_by** | **str** |  | [optional] 
**workspace_id** | **str** |  | 
**amenity_id** | **int** |  | 

## Example

```python
from workspace_sdk.models.feature import Feature

# TODO update the JSON string below
json = "{}"
# create an instance of Feature from a JSON string
feature_instance = Feature.from_json(json)
# print the JSON string representation of the object
print(Feature.to_json())

# convert the object into a dict
feature_dict = feature_instance.to_dict()
# create an instance of Feature from a dict
feature_from_dict = Feature.from_dict(feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


