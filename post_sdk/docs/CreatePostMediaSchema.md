# CreatePostMediaSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_id** | **int** |  | 
**media_id** | **str** |  | 
**alt_text** | **str** |  | [optional] 

## Example

```python
from post_sdk.models.create_post_media_schema import CreatePostMediaSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePostMediaSchema from a JSON string
create_post_media_schema_instance = CreatePostMediaSchema.from_json(json)
# print the JSON string representation of the object
print(CreatePostMediaSchema.to_json())

# convert the object into a dict
create_post_media_schema_dict = create_post_media_schema_instance.to_dict()
# create an instance of CreatePostMediaSchema from a dict
create_post_media_schema_from_dict = CreatePostMediaSchema.from_dict(create_post_media_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


