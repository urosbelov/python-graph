# VerifyIdentifierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** |  | 
**device_id** | **str** |  | 
**otp_code** | **str** |  | 

## Example

```python
from identity_sdk.models.verify_identifier_request import VerifyIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyIdentifierRequest from a JSON string
verify_identifier_request_instance = VerifyIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyIdentifierRequest.to_json())

# convert the object into a dict
verify_identifier_request_dict = verify_identifier_request_instance.to_dict()
# create an instance of VerifyIdentifierRequest from a dict
verify_identifier_request_from_dict = VerifyIdentifierRequest.from_dict(verify_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


