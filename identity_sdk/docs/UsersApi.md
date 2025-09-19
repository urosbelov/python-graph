# identity_sdk.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](UsersApi.md#activate_user) | **POST** /users/{user_id}/activate | Activate User
[**create_user**](UsersApi.md#create_user) | **POST** /users/ | Create User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Delete User
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{user_id} | Get User By Id
[**get_users_batch**](UsersApi.md#get_users_batch) | **POST** /users/batch | Get Users Batch
[**list_users**](UsersApi.md#list_users) | **POST** /users/list | List Users
[**suspend_user**](UsersApi.md#suspend_user) | **POST** /users/{user_id}/suspend | Suspend User
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user_id} | Update User


# **activate_user**
> activate_user(user_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Activate User

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
    api_instance = identity_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Activate User
        api_instance.activate_user(user_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling UsersApi->activate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **create_user**
> UserCreateAdminResponse create_user(user_create_admin_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create User

### Example


```python
import identity_sdk
from identity_sdk.models.user_create_admin_request import UserCreateAdminRequest
from identity_sdk.models.user_create_admin_response import UserCreateAdminResponse
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
    api_instance = identity_sdk.UsersApi(api_client)
    user_create_admin_request = identity_sdk.UserCreateAdminRequest() # UserCreateAdminRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Create User
        api_response = api_instance.create_user(user_create_admin_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_admin_request** | [**UserCreateAdminRequest**](UserCreateAdminRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**UserCreateAdminResponse**](UserCreateAdminResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Delete User

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
    api_instance = identity_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Delete User
        api_instance.delete_user(user_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **get_user_by_id**
> UserResponse get_user_by_id(user_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get User By Id

### Example


```python
import identity_sdk
from identity_sdk.models.user_response import UserResponse
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
    api_instance = identity_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get User By Id
        api_response = api_instance.get_user_by_id(user_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of UsersApi->get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_users_batch**
> GetUsersBatchResponse get_users_batch(get_users_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Users Batch

### Example


```python
import identity_sdk
from identity_sdk.models.get_users_batch_request import GetUsersBatchRequest
from identity_sdk.models.get_users_batch_response import GetUsersBatchResponse
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
    api_instance = identity_sdk.UsersApi(api_client)
    get_users_batch_request = identity_sdk.GetUsersBatchRequest() # GetUsersBatchRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Users Batch
        api_response = api_instance.get_users_batch(get_users_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of UsersApi->get_users_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_users_batch_request** | [**GetUsersBatchRequest**](GetUsersBatchRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**GetUsersBatchResponse**](GetUsersBatchResponse.md)

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

# **list_users**
> ListUsersResponse list_users(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_users_request=list_users_request)

List Users

### Example


```python
import identity_sdk
from identity_sdk.models.list_users_request import ListUsersRequest
from identity_sdk.models.list_users_response import ListUsersResponse
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
    api_instance = identity_sdk.UsersApi(api_client)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)
    list_users_request = identity_sdk.ListUsersRequest() # ListUsersRequest |  (optional)

    try:
        # List Users
        api_response = api_instance.list_users(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_users_request=list_users_request)
        print("The response of UsersApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 
 **list_users_request** | [**ListUsersRequest**](ListUsersRequest.md)|  | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

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

# **suspend_user**
> suspend_user(user_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Suspend User

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
    api_instance = identity_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Suspend User
        api_instance.suspend_user(user_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling UsersApi->suspend_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **update_user**
> UserResponse update_user(user_id, user_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Update User

### Example


```python
import identity_sdk
from identity_sdk.models.user_response import UserResponse
from identity_sdk.models.user_update import UserUpdate
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
    api_instance = identity_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    user_update = identity_sdk.UserUpdate() # UserUpdate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Update User
        api_response = api_instance.update_user(user_id, user_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

