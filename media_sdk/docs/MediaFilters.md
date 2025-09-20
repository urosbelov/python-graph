# MediaFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**MediaStatus**](MediaStatus.md) |  | [optional] 
**owner_service** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**category** | [**MediaCategory**](MediaCategory.md) |  | [optional] 

## Example

```python
from media_sdk.models.media_filters import MediaFilters

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFilters from a JSON string
media_filters_instance = MediaFilters.from_json(json)
# print the JSON string representation of the object
print(MediaFilters.to_json())

# convert the object into a dict
media_filters_dict = media_filters_instance.to_dict()
# create an instance of MediaFilters from a dict
media_filters_from_dict = MediaFilters.from_dict(media_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


