# CreatePostSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 

## Example

```python
from post_sdk.models.create_post_schema import CreatePostSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePostSchema from a JSON string
create_post_schema_instance = CreatePostSchema.from_json(json)
# print the JSON string representation of the object
print(CreatePostSchema.to_json())

# convert the object into a dict
create_post_schema_dict = create_post_schema_instance.to_dict()
# create an instance of CreatePostSchema from a dict
create_post_schema_from_dict = CreatePostSchema.from_dict(create_post_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


