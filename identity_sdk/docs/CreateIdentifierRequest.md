# CreateIdentifierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from identity_sdk.models.create_identifier_request import CreateIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIdentifierRequest from a JSON string
create_identifier_request_instance = CreateIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(CreateIdentifierRequest.to_json())

# convert the object into a dict
create_identifier_request_dict = create_identifier_request_instance.to_dict()
# create an instance of CreateIdentifierRequest from a dict
create_identifier_request_from_dict = CreateIdentifierRequest.from_dict(create_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


