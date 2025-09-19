# GetPostsBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | **Dict[str, List[Post]]** |  | 

## Example

```python
from post_sdk.models.get_posts_batch_response import GetPostsBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostsBatchResponse from a JSON string
get_posts_batch_response_instance = GetPostsBatchResponse.from_json(json)
# print the JSON string representation of the object
print(GetPostsBatchResponse.to_json())

# convert the object into a dict
get_posts_batch_response_dict = get_posts_batch_response_instance.to_dict()
# create an instance of GetPostsBatchResponse from a dict
get_posts_batch_response_from_dict = GetPostsBatchResponse.from_dict(get_posts_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


