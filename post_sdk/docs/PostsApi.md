# post_sdk.PostsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_post**](PostsApi.md#create_post) | **POST** /posts/ | Create Post
[**delete_post**](PostsApi.md#delete_post) | **DELETE** /posts/{post_id} | Delete Post
[**flag_post**](PostsApi.md#flag_post) | **POST** /posts/{post_id}/flag | Flag Post
[**get_post**](PostsApi.md#get_post) | **GET** /posts/{post_id} | Get Post
[**get_posts_batch**](PostsApi.md#get_posts_batch) | **POST** /posts/batch | Get Posts Batch
[**list_posts**](PostsApi.md#list_posts) | **POST** /posts/list | List Posts
[**publish_post**](PostsApi.md#publish_post) | **POST** /posts/{post_id}/publish | Publish Post


# **create_post**
> Post create_post(create_post_schema, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create Post

### Example


```python
import post_sdk
from post_sdk.models.create_post_schema import CreatePostSchema
from post_sdk.models.post import Post
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
    api_instance = post_sdk.PostsApi(api_client)
    create_post_schema = post_sdk.CreatePostSchema() # CreatePostSchema | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Create Post
        api_response = api_instance.create_post(create_post_schema, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of PostsApi->create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_post_schema** | [**CreatePostSchema**](CreatePostSchema.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**Post**](Post.md)

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

# **delete_post**
> delete_post(post_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Delete Post

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
    api_instance = post_sdk.PostsApi(api_client)
    post_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Delete Post
        api_instance.delete_post(post_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling PostsApi->delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **int**|  | 
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

# **flag_post**
> flag_post(post_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Flag Post

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
    api_instance = post_sdk.PostsApi(api_client)
    post_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Flag Post
        api_instance.flag_post(post_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling PostsApi->flag_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **int**|  | 
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

# **get_post**
> Post get_post(post_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Post

### Example


```python
import post_sdk
from post_sdk.models.post import Post
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
    api_instance = post_sdk.PostsApi(api_client)
    post_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Post
        api_response = api_instance.get_post(post_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of PostsApi->get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**Post**](Post.md)

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

# **get_posts_batch**
> GetPostsBatchResponse get_posts_batch(get_posts_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Posts Batch

### Example


```python
import post_sdk
from post_sdk.models.get_posts_batch_request import GetPostsBatchRequest
from post_sdk.models.get_posts_batch_response import GetPostsBatchResponse
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
    api_instance = post_sdk.PostsApi(api_client)
    get_posts_batch_request = post_sdk.GetPostsBatchRequest() # GetPostsBatchRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Posts Batch
        api_response = api_instance.get_posts_batch(get_posts_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of PostsApi->get_posts_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->get_posts_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_posts_batch_request** | [**GetPostsBatchRequest**](GetPostsBatchRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**GetPostsBatchResponse**](GetPostsBatchResponse.md)

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

# **list_posts**
> ListPostsResponse list_posts(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_posts_request=list_posts_request)

List Posts

### Example


```python
import post_sdk
from post_sdk.models.list_posts_request import ListPostsRequest
from post_sdk.models.list_posts_response import ListPostsResponse
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
    api_instance = post_sdk.PostsApi(api_client)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)
    list_posts_request = post_sdk.ListPostsRequest() # ListPostsRequest |  (optional)

    try:
        # List Posts
        api_response = api_instance.list_posts(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_posts_request=list_posts_request)
        print("The response of PostsApi->list_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostsApi->list_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 
 **list_posts_request** | [**ListPostsRequest**](ListPostsRequest.md)|  | [optional] 

### Return type

[**ListPostsResponse**](ListPostsResponse.md)

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

# **publish_post**
> publish_post(post_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Publish Post

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
    api_instance = post_sdk.PostsApi(api_client)
    post_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Publish Post
        api_instance.publish_post(post_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling PostsApi->publish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **int**|  | 
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

