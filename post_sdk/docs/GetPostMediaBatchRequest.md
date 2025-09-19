# GetPostMediaBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_ids** | **List[str]** |  | 

## Example

```python
from post_sdk.models.get_post_media_batch_request import GetPostMediaBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostMediaBatchRequest from a JSON string
get_post_media_batch_request_instance = GetPostMediaBatchRequest.from_json(json)
# print the JSON string representation of the object
print(GetPostMediaBatchRequest.to_json())

# convert the object into a dict
get_post_media_batch_request_dict = get_post_media_batch_request_instance.to_dict()
# create an instance of GetPostMediaBatchRequest from a dict
get_post_media_batch_request_from_dict = GetPostMediaBatchRequest.from_dict(get_post_media_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


