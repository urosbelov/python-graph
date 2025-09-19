# CategoryFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CategoryStatus**](CategoryStatus.md) |  | [optional] 
**name** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from workspace_sdk.models.category_filters import CategoryFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryFilters from a JSON string
category_filters_instance = CategoryFilters.from_json(json)
# print the JSON string representation of the object
print(CategoryFilters.to_json())

# convert the object into a dict
category_filters_dict = category_filters_instance.to_dict()
# create an instance of CategoryFilters from a dict
category_filters_from_dict = CategoryFilters.from_dict(category_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


