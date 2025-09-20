# GetSignedUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**MediaCategory**](MediaCategory.md) |  | 
**owner_id** | **str** |  | 
**mime_type** | **str** |  | 

## Example

```python
from media_sdk.models.get_signed_url_request import GetSignedUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignedUrlRequest from a JSON string
get_signed_url_request_instance = GetSignedUrlRequest.from_json(json)
# print the JSON string representation of the object
print(GetSignedUrlRequest.to_json())

# convert the object into a dict
get_signed_url_request_dict = get_signed_url_request_instance.to_dict()
# create an instance of GetSignedUrlRequest from a dict
get_signed_url_request_from_dict = GetSignedUrlRequest.from_dict(get_signed_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


