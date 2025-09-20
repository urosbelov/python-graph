# GetSignedUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_url** | **str** |  | 
**media_id** | **str** |  | 

## Example

```python
from media_sdk.models.get_signed_url_response import GetSignedUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSignedUrlResponse from a JSON string
get_signed_url_response_instance = GetSignedUrlResponse.from_json(json)
# print the JSON string representation of the object
print(GetSignedUrlResponse.to_json())

# convert the object into a dict
get_signed_url_response_dict = get_signed_url_response_instance.to_dict()
# create an instance of GetSignedUrlResponse from a dict
get_signed_url_response_from_dict = GetSignedUrlResponse.from_dict(get_signed_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


