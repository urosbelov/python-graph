# media_sdk.MediaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media**](MediaApi.md#delete_media) | **DELETE** /media/{media_id} | Delete Media
[**get_media_batch**](MediaApi.md#get_media_batch) | **POST** /media/batch | Get Media Batch
[**get_media_by_id**](MediaApi.md#get_media_by_id) | **GET** /media/{media_id} | Get Media By Id
[**get_signed_url**](MediaApi.md#get_signed_url) | **POST** /media/get-signed-url | Get Signed Url
[**list_media**](MediaApi.md#list_media) | **POST** /media/list | List Media
[**process**](MediaApi.md#process) | **POST** /media/{media_id}/process | Process


# **delete_media**
> delete_media(media_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Delete Media

### Example


```python
import media_sdk
from media_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = media_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with media_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_sdk.MediaApi(api_client)
    media_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Delete Media
        api_instance.delete_media(media_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling MediaApi->delete_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**|  | 
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

# **get_media_batch**
> GetMediaBatchResponse get_media_batch(get_media_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Media Batch

### Example


```python
import media_sdk
from media_sdk.models.get_media_batch_request import GetMediaBatchRequest
from media_sdk.models.get_media_batch_response import GetMediaBatchResponse
from media_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = media_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with media_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_sdk.MediaApi(api_client)
    get_media_batch_request = media_sdk.GetMediaBatchRequest() # GetMediaBatchRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Media Batch
        api_response = api_instance.get_media_batch(get_media_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of MediaApi->get_media_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_media_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_media_batch_request** | [**GetMediaBatchRequest**](GetMediaBatchRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**GetMediaBatchResponse**](GetMediaBatchResponse.md)

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

# **get_media_by_id**
> Media get_media_by_id(media_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Media By Id

### Example


```python
import media_sdk
from media_sdk.models.media import Media
from media_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = media_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with media_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_sdk.MediaApi(api_client)
    media_id = 'media_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Media By Id
        api_response = api_instance.get_media_by_id(media_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of MediaApi->get_media_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_media_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**Media**](Media.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signed_url**
> GetSignedUrlResponse get_signed_url(get_signed_url_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Signed Url

### Example


```python
import media_sdk
from media_sdk.models.get_signed_url_request import GetSignedUrlRequest
from media_sdk.models.get_signed_url_response import GetSignedUrlResponse
from media_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = media_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with media_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_sdk.MediaApi(api_client)
    get_signed_url_request = media_sdk.GetSignedUrlRequest() # GetSignedUrlRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Signed Url
        api_response = api_instance.get_signed_url(get_signed_url_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of MediaApi->get_signed_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_signed_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_signed_url_request** | [**GetSignedUrlRequest**](GetSignedUrlRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**GetSignedUrlResponse**](GetSignedUrlResponse.md)

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

# **list_media**
> ListMediaResponse list_media(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_media_request=list_media_request)

List Media

### Example


```python
import media_sdk
from media_sdk.models.list_media_request import ListMediaRequest
from media_sdk.models.list_media_response import ListMediaResponse
from media_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = media_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with media_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_sdk.MediaApi(api_client)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)
    list_media_request = media_sdk.ListMediaRequest() # ListMediaRequest |  (optional)

    try:
        # List Media
        api_response = api_instance.list_media(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_media_request=list_media_request)
        print("The response of MediaApi->list_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->list_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 
 **list_media_request** | [**ListMediaRequest**](ListMediaRequest.md)|  | [optional] 

### Return type

[**ListMediaResponse**](ListMediaResponse.md)

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

# **process**
> process(media_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Process

### Example


```python
import media_sdk
from media_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = media_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with media_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_sdk.MediaApi(api_client)
    media_id = 'media_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Process
        api_instance.process(media_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling MediaApi->process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**|  | 
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

