# CreateFeatureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**amenity_id** | **int** |  | 

## Example

```python
from workspace_sdk.models.create_feature_request import CreateFeatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeatureRequest from a JSON string
create_feature_request_instance = CreateFeatureRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFeatureRequest.to_json())

# convert the object into a dict
create_feature_request_dict = create_feature_request_instance.to_dict()
# create an instance of CreateFeatureRequest from a dict
create_feature_request_from_dict = CreateFeatureRequest.from_dict(create_feature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


