# identity_sdk.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_session**](SessionsApi.md#delete_session) | **DELETE** /sessions/{session_id} | Delete Session
[**get_session**](SessionsApi.md#get_session) | **GET** /sessions/{session_id} | Get Sessions
[**get_user_sessions**](SessionsApi.md#get_user_sessions) | **GET** /sessions/user/{user_id} | Get User Sessions


# **delete_session**
> delete_session(session_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Delete Session

### Example


```python
import identity_sdk
from identity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = identity_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with identity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = identity_sdk.SessionsApi(api_client)
    session_id = 'session_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Delete Session
        api_instance.delete_session(session_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling SessionsApi->delete_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

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

# **get_session**
> SessionResponse get_session(session_id)

Get Sessions

### Example


```python
import identity_sdk
from identity_sdk.models.session_response import SessionResponse
from identity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = identity_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with identity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = identity_sdk.SessionsApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Get Sessions
        api_response = api_instance.get_session(session_id)
        print("The response of SessionsApi->get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**SessionResponse**](SessionResponse.md)

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

# **get_user_sessions**
> List[SessionResponse] get_user_sessions(user_id)

Get User Sessions

### Example


```python
import identity_sdk
from identity_sdk.models.session_response import SessionResponse
from identity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = identity_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with identity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = identity_sdk.SessionsApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User Sessions
        api_response = api_instance.get_user_sessions(user_id)
        print("The response of SessionsApi->get_user_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->get_user_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[SessionResponse]**](SessionResponse.md)

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

