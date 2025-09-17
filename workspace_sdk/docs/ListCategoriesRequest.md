# ListCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**CategoryFilters**](CategoryFilters.md) |  | [optional] 
**pagination** | [**PageRequest**](PageRequest.md) |  | [optional] 

## Example

```python
from workspace_sdk.models.list_categories_request import ListCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListCategoriesRequest from a JSON string
list_categories_request_instance = ListCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(ListCategoriesRequest.to_json())

# convert the object into a dict
list_categories_request_dict = list_categories_request_instance.to_dict()
# create an instance of ListCategoriesRequest from a dict
list_categories_request_from_dict = ListCategoriesRequest.from_dict(list_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


