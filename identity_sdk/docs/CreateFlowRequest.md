# CreateFlowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**metadata** | [**FlowMetadata**](FlowMetadata.md) |  | 

## Example

```python
from identity_sdk.models.create_flow_request import CreateFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFlowRequest from a JSON string
create_flow_request_instance = CreateFlowRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFlowRequest.to_json())

# convert the object into a dict
create_flow_request_dict = create_flow_request_instance.to_dict()
# create an instance of CreateFlowRequest from a dict
create_flow_request_from_dict = CreateFlowRequest.from_dict(create_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


