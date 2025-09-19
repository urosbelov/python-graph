# PostFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PostStatus**](PostStatus.md) |  | [optional] 

## Example

```python
from post_sdk.models.post_filters import PostFilters

# TODO update the JSON string below
json = "{}"
# create an instance of PostFilters from a JSON string
post_filters_instance = PostFilters.from_json(json)
# print the JSON string representation of the object
print(PostFilters.to_json())

# convert the object into a dict
post_filters_dict = post_filters_instance.to_dict()
# create an instance of PostFilters from a dict
post_filters_from_dict = PostFilters.from_dict(post_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


