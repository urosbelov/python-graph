# BBox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**north_east** | [**LatLng**](LatLng.md) |  | 
**south_west** | [**LatLng**](LatLng.md) |  | 

## Example

```python
from workspace_sdk.models.b_box import BBox

# TODO update the JSON string below
json = "{}"
# create an instance of BBox from a JSON string
b_box_instance = BBox.from_json(json)
# print the JSON string representation of the object
print(BBox.to_json())

# convert the object into a dict
b_box_dict = b_box_instance.to_dict()
# create an instance of BBox from a dict
b_box_from_dict = BBox.from_dict(b_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


