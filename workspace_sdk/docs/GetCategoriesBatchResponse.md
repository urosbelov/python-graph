# GetCategoriesBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**Dict[str, Category]**](Category.md) |  | 

## Example

```python
from workspace_sdk.models.get_categories_batch_response import GetCategoriesBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCategoriesBatchResponse from a JSON string
get_categories_batch_response_instance = GetCategoriesBatchResponse.from_json(json)
# print the JSON string representation of the object
print(GetCategoriesBatchResponse.to_json())

# convert the object into a dict
get_categories_batch_response_dict = get_categories_batch_response_instance.to_dict()
# create an instance of GetCategoriesBatchResponse from a dict
get_categories_batch_response_from_dict = GetCategoriesBatchResponse.from_dict(get_categories_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


