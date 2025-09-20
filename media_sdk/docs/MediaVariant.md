# MediaVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**format** | **str** |  | 
**width** | **int** |  | 
**height** | **int** |  | 
**size_bytes** | **int** |  | 
**quality** | **float** |  | 

## Example

```python
from media_sdk.models.media_variant import MediaVariant

# TODO update the JSON string below
json = "{}"
# create an instance of MediaVariant from a JSON string
media_variant_instance = MediaVariant.from_json(json)
# print the JSON string representation of the object
print(MediaVariant.to_json())

# convert the object into a dict
media_variant_dict = media_variant_instance.to_dict()
# create an instance of MediaVariant from a dict
media_variant_from_dict = MediaVariant.from_dict(media_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


