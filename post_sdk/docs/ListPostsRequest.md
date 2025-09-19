# ListPostsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**PostFilters**](PostFilters.md) |  | [optional] 
**pagination** | [**PageRequest**](PageRequest.md) |  | [optional] 

## Example

```python
from post_sdk.models.list_posts_request import ListPostsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListPostsRequest from a JSON string
list_posts_request_instance = ListPostsRequest.from_json(json)
# print the JSON string representation of the object
print(ListPostsRequest.to_json())

# convert the object into a dict
list_posts_request_dict = list_posts_request_instance.to_dict()
# create an instance of ListPostsRequest from a dict
list_posts_request_from_dict = ListPostsRequest.from_dict(list_posts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


