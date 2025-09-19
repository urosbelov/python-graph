# ValidateFlowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FlowType**](FlowType.md) |  | 
**flow_id** | **str** |  | 
**step** | [**FlowStep**](FlowStep.md) |  | 
**device_id** | **str** |  | 

## Example

```python
from identity_sdk.models.validate_flow_request import ValidateFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateFlowRequest from a JSON string
validate_flow_request_instance = ValidateFlowRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateFlowRequest.to_json())

# convert the object into a dict
validate_flow_request_dict = validate_flow_request_instance.to_dict()
# create an instance of ValidateFlowRequest from a dict
validate_flow_request_from_dict = ValidateFlowRequest.from_dict(validate_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


