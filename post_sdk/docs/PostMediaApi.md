# post_sdk.PostMediaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_post_media**](PostMediaApi.md#create_post_media) | **POST** /post-media/ | Create Post Media
[**delete_post_media**](PostMediaApi.md#delete_post_media) | **DELETE** /post-media/{post_media_id} | Delete Post Media
[**get_post_media_batch**](PostMediaApi.md#get_post_media_batch) | **POST** /post-media/batch | Get Post Media Batch


# **create_post_media**
> PostMedia create_post_media(create_post_media_schema, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create Post Media

### Example


```python
import post_sdk
from post_sdk.models.create_post_media_schema import CreatePostMediaSchema
from post_sdk.models.post_media import PostMedia
from post_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = post_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with post_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = post_sdk.PostMediaApi(api_client)
    create_post_media_schema = post_sdk.CreatePostMediaSchema() # CreatePostMediaSchema | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Create Post Media
        api_response = api_instance.create_post_media(create_post_media_schema, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of PostMediaApi->create_post_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostMediaApi->create_post_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_post_media_schema** | [**CreatePostMediaSchema**](CreatePostMediaSchema.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**PostMedia**](PostMedia.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_post_media**
> delete_post_media(post_media_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Delete Post Media

### Example


```python
import post_sdk
from post_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = post_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with post_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = post_sdk.PostMediaApi(api_client)
    post_media_id = 'post_media_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Delete Post Media
        api_instance.delete_post_media(post_media_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling PostMediaApi->delete_post_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_media_id** | **str**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_media_batch**
> GetPostMediaBatchResponse get_post_media_batch(get_post_media_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Post Media Batch

### Example


```python
import post_sdk
from post_sdk.models.get_post_media_batch_request import GetPostMediaBatchRequest
from post_sdk.models.get_post_media_batch_response import GetPostMediaBatchResponse
from post_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = post_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with post_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = post_sdk.PostMediaApi(api_client)
    get_post_media_batch_request = post_sdk.GetPostMediaBatchRequest() # GetPostMediaBatchRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Post Media Batch
        api_response = api_instance.get_post_media_batch(get_post_media_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of PostMediaApi->get_post_media_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostMediaApi->get_post_media_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_post_media_batch_request** | [**GetPostMediaBatchRequest**](GetPostMediaBatchRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**GetPostMediaBatchResponse**](GetPostMediaBatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

