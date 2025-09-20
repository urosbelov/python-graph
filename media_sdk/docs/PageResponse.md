# PageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | 
**has_next_page** | **bool** |  | 
**has_previous_page** | **bool** |  | 

## Example

```python
from media_sdk.models.page_response import PageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageResponse from a JSON string
page_response_instance = PageResponse.from_json(json)
# print the JSON string representation of the object
print(PageResponse.to_json())

# convert the object into a dict
page_response_dict = page_response_instance.to_dict()
# create an instance of PageResponse from a dict
page_response_from_dict = PageResponse.from_dict(page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


