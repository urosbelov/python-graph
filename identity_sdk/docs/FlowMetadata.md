# FlowMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | 
**browser** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from identity_sdk.models.flow_metadata import FlowMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowMetadata from a JSON string
flow_metadata_instance = FlowMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowMetadata.to_json())

# convert the object into a dict
flow_metadata_dict = flow_metadata_instance.to_dict()
# create an instance of FlowMetadata from a dict
flow_metadata_from_dict = FlowMetadata.from_dict(flow_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


