# Media


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | [**MediaStatus**](MediaStatus.md) |  | [optional] 
**variants** | [**Dict[str, MediaVariant]**](MediaVariant.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**category** | [**MediaCategory**](MediaCategory.md) |  | 
**object_key** | **str** |  | 
**owner_id** | **str** |  | 
**mime_type** | **str** |  | [optional] 
**size_bytes** | **int** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**quality** | **float** |  | [optional] 
**reference_count** | **int** |  | [optional] [default to 1]
**checksum** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from media_sdk.models.media import Media

# TODO update the JSON string below
json = "{}"
# create an instance of Media from a JSON string
media_instance = Media.from_json(json)
# print the JSON string representation of the object
print(Media.to_json())

# convert the object into a dict
media_dict = media_instance.to_dict()
# create an instance of Media from a dict
media_from_dict = Media.from_dict(media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


