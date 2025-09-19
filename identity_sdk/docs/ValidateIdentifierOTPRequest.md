# ValidateIdentifierOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_id** | **str** |  | 
**otp_code** | **int** | 6-digit OTP code | 

## Example

```python
from identity_sdk.models.validate_identifier_otp_request import ValidateIdentifierOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateIdentifierOTPRequest from a JSON string
validate_identifier_otp_request_instance = ValidateIdentifierOTPRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateIdentifierOTPRequest.to_json())

# convert the object into a dict
validate_identifier_otp_request_dict = validate_identifier_otp_request_instance.to_dict()
# create an instance of ValidateIdentifierOTPRequest from a dict
validate_identifier_otp_request_from_dict = ValidateIdentifierOTPRequest.from_dict(validate_identifier_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


