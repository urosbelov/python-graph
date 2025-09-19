# Post


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**base62_id** | **str** |  | [optional] 
**status** | [**PostStatus**](PostStatus.md) |  | [optional] 
**created_by** | **str** |  | [optional] 
**workspace_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**flagged_at** | **datetime** |  | [optional] 
**published_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**view_count** | **int** |  | [optional] [default to 0]
**place_id** | **str** |  | [optional] 
**source_id** | **str** |  | [readonly] 
**source_type** | [**PostSourceType**](PostSourceType.md) |  | [readonly] 

## Example

```python
from post_sdk.models.post import Post

# TODO update the JSON string below
json = "{}"
# create an instance of Post from a JSON string
post_instance = Post.from_json(json)
# print the JSON string representation of the object
print(Post.to_json())

# convert the object into a dict
post_dict = post_instance.to_dict()
# create an instance of Post from a dict
post_from_dict = Post.from_dict(post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


