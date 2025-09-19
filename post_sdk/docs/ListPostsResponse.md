# ListPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | [**List[Post]**](Post.md) |  | 
**pagination** | [**PageResponse**](PageResponse.md) |  | 

## Example

```python
from post_sdk.models.list_posts_response import ListPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPostsResponse from a JSON string
list_posts_response_instance = ListPostsResponse.from_json(json)
# print the JSON string representation of the object
print(ListPostsResponse.to_json())

# convert the object into a dict
list_posts_response_dict = list_posts_response_instance.to_dict()
# create an instance of ListPostsResponse from a dict
list_posts_response_from_dict = ListPostsResponse.from_dict(list_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


