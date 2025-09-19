# IdentifierResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**type** | [**IdentifierType**](IdentifierType.md) |  | 
**value** | **str** |  | 
**validated** | **bool** |  | 
**is_default** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from identity_sdk.models.identifier_response import IdentifierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifierResponse from a JSON string
identifier_response_instance = IdentifierResponse.from_json(json)
# print the JSON string representation of the object
print(IdentifierResponse.to_json())

# convert the object into a dict
identifier_response_dict = identifier_response_instance.to_dict()
# create an instance of IdentifierResponse from a dict
identifier_response_from_dict = IdentifierResponse.from_dict(identifier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


