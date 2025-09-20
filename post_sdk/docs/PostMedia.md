# PostMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**post_id** | **int** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**alt_text** | **str** |  | [optional] 
**media_id** | **str** |  | 

## Example

```python
from post_sdk.models.post_media import PostMedia

# TODO update the JSON string below
json = "{}"
# create an instance of PostMedia from a JSON string
post_media_instance = PostMedia.from_json(json)
# print the JSON string representation of the object
print(PostMedia.to_json())

# convert the object into a dict
post_media_dict = post_media_instance.to_dict()
# create an instance of PostMedia from a dict
post_media_from_dict = PostMedia.from_dict(post_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


