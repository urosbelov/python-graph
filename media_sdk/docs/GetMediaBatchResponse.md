# GetMediaBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **Dict[str, List[Media]]** |  | 

## Example

```python
from media_sdk.models.get_media_batch_response import GetMediaBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMediaBatchResponse from a JSON string
get_media_batch_response_instance = GetMediaBatchResponse.from_json(json)
# print the JSON string representation of the object
print(GetMediaBatchResponse.to_json())

# convert the object into a dict
get_media_batch_response_dict = get_media_batch_response_instance.to_dict()
# create an instance of GetMediaBatchResponse from a dict
get_media_batch_response_from_dict = GetMediaBatchResponse.from_dict(get_media_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


