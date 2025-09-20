# ListMediaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Media]**](Media.md) |  | 
**pagination** | [**PageResponse**](PageResponse.md) |  | 

## Example

```python
from media_sdk.models.list_media_response import ListMediaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMediaResponse from a JSON string
list_media_response_instance = ListMediaResponse.from_json(json)
# print the JSON string representation of the object
print(ListMediaResponse.to_json())

# convert the object into a dict
list_media_response_dict = list_media_response_instance.to_dict()
# create an instance of ListMediaResponse from a dict
list_media_response_from_dict = ListMediaResponse.from_dict(list_media_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


