# GetPostMediaBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_media** | **Dict[str, List[PostMedia]]** |  | 

## Example

```python
from post_sdk.models.get_post_media_batch_response import GetPostMediaBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostMediaBatchResponse from a JSON string
get_post_media_batch_response_instance = GetPostMediaBatchResponse.from_json(json)
# print the JSON string representation of the object
print(GetPostMediaBatchResponse.to_json())

# convert the object into a dict
get_post_media_batch_response_dict = get_post_media_batch_response_instance.to_dict()
# create an instance of GetPostMediaBatchResponse from a dict
get_post_media_batch_response_from_dict = GetPostMediaBatchResponse.from_dict(get_post_media_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


