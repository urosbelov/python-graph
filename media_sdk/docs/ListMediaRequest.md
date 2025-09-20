# ListMediaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**MediaFilters**](MediaFilters.md) |  | [optional] 
**pagination** | [**PageRequest**](PageRequest.md) |  | [optional] 

## Example

```python
from media_sdk.models.list_media_request import ListMediaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListMediaRequest from a JSON string
list_media_request_instance = ListMediaRequest.from_json(json)
# print the JSON string representation of the object
print(ListMediaRequest.to_json())

# convert the object into a dict
list_media_request_dict = list_media_request_instance.to_dict()
# create an instance of ListMediaRequest from a dict
list_media_request_from_dict = ListMediaRequest.from_dict(list_media_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


