# ValidateIdentifierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** |  | 
**device_id** | **str** |  | 
**identifier** | **str** |  | 

## Example

```python
from identity_sdk.models.validate_identifier_request import ValidateIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateIdentifierRequest from a JSON string
validate_identifier_request_instance = ValidateIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateIdentifierRequest.to_json())

# convert the object into a dict
validate_identifier_request_dict = validate_identifier_request_instance.to_dict()
# create an instance of ValidateIdentifierRequest from a dict
validate_identifier_request_from_dict = ValidateIdentifierRequest.from_dict(validate_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


