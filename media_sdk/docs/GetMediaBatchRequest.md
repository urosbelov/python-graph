# GetMediaBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_ids** | **List[str]** |  | 

## Example

```python
from media_sdk.models.get_media_batch_request import GetMediaBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMediaBatchRequest from a JSON string
get_media_batch_request_instance = GetMediaBatchRequest.from_json(json)
# print the JSON string representation of the object
print(GetMediaBatchRequest.to_json())

# convert the object into a dict
get_media_batch_request_dict = get_media_batch_request_instance.to_dict()
# create an instance of GetMediaBatchRequest from a dict
get_media_batch_request_from_dict = GetMediaBatchRequest.from_dict(get_media_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


