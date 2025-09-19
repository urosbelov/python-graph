# GetCategoriesBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_ids** | **List[int]** |  | 

## Example

```python
from workspace_sdk.models.get_categories_batch_request import GetCategoriesBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCategoriesBatchRequest from a JSON string
get_categories_batch_request_instance = GetCategoriesBatchRequest.from_json(json)
# print the JSON string representation of the object
print(GetCategoriesBatchRequest.to_json())

# convert the object into a dict
get_categories_batch_request_dict = get_categories_batch_request_instance.to_dict()
# create an instance of GetCategoriesBatchRequest from a dict
get_categories_batch_request_from_dict = GetCategoriesBatchRequest.from_dict(get_categories_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


