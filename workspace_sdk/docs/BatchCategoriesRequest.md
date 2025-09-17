# BatchCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 

## Example

```python
from workspace_sdk.models.batch_categories_request import BatchCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCategoriesRequest from a JSON string
batch_categories_request_instance = BatchCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(BatchCategoriesRequest.to_json())

# convert the object into a dict
batch_categories_request_dict = batch_categories_request_instance.to_dict()
# create an instance of BatchCategoriesRequest from a dict
batch_categories_request_from_dict = BatchCategoriesRequest.from_dict(batch_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


