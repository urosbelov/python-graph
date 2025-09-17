# workspace_sdk.WorkspacesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_workspaces**](WorkspacesApi.md#batch_workspaces) | **POST** /workspaces/batch | Get Workspaces By Ids
[**bbox_query**](WorkspacesApi.md#bbox_query) | **POST** /workspaces/bbox | Bbox Query
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /workspaces/ | Create Workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspace_id} | Delete Workspace
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace_id} | Get Workspace
[**get_workspace_by_handle**](WorkspacesApi.md#get_workspace_by_handle) | **GET** /workspaces/handle/{handle} | Get Workspace By Handle
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **POST** /workspaces/list | List Workspaces
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{workspace_id} | Update Workspace
[**update_workspace_status**](WorkspacesApi.md#update_workspace_status) | **POST** /workspaces/{workspace_id}/status | Update Workspace Status
[**validate_workspace_exists**](WorkspacesApi.md#validate_workspace_exists) | **GET** /workspaces/{workspace_id}/exist | Validate Workspace Exists


# **batch_workspaces**
> BatchWorkspacesResponse batch_workspaces(batch_workspaces_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Workspaces By Ids

### Example


```python
import workspace_sdk
from workspace_sdk.models.batch_workspaces_request import BatchWorkspacesRequest
from workspace_sdk.models.batch_workspaces_response import BatchWorkspacesResponse
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    batch_workspaces_request = workspace_sdk.BatchWorkspacesRequest() # BatchWorkspacesRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Workspaces By Ids
        api_response = api_instance.batch_workspaces(batch_workspaces_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of WorkspacesApi->batch_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->batch_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_workspaces_request** | [**BatchWorkspacesRequest**](BatchWorkspacesRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**BatchWorkspacesResponse**](BatchWorkspacesResponse.md)

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

# **bbox_query**
> List[WorkspaceResponse] bbox_query(x_user_id=x_user_id, x_workspace_id=x_workspace_id, workspace_b_box_query=workspace_b_box_query)

Bbox Query

### Example


```python
import workspace_sdk
from workspace_sdk.models.workspace_b_box_query import WorkspaceBBoxQuery
from workspace_sdk.models.workspace_response import WorkspaceResponse
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)
    workspace_b_box_query = workspace_sdk.WorkspaceBBoxQuery() # WorkspaceBBoxQuery |  (optional)

    try:
        # Bbox Query
        api_response = api_instance.bbox_query(x_user_id=x_user_id, x_workspace_id=x_workspace_id, workspace_b_box_query=workspace_b_box_query)
        print("The response of WorkspacesApi->bbox_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->bbox_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 
 **workspace_b_box_query** | [**WorkspaceBBoxQuery**](WorkspaceBBoxQuery.md)|  | [optional] 

### Return type

[**List[WorkspaceResponse]**](WorkspaceResponse.md)

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

# **create_workspace**
> WorkspaceResponse create_workspace(workspace_create, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create Workspace

### Example


```python
import workspace_sdk
from workspace_sdk.models.workspace_create import WorkspaceCreate
from workspace_sdk.models.workspace_response import WorkspaceResponse
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    workspace_create = workspace_sdk.WorkspaceCreate() # WorkspaceCreate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Create Workspace
        api_response = api_instance.create_workspace(workspace_create, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of WorkspacesApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_create** | [**WorkspaceCreate**](WorkspaceCreate.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

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

# **delete_workspace**
> delete_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Delete Workspace

### Example


```python
import workspace_sdk
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Delete Workspace
        api_instance.delete_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
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

# **get_workspace**
> WorkspaceResponse get_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Workspace

### Example


```python
import workspace_sdk
from workspace_sdk.models.workspace_response import WorkspaceResponse
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Workspace
        api_response = api_instance.get_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of WorkspacesApi->get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

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

# **get_workspace_by_handle**
> WorkspaceResponse get_workspace_by_handle(handle, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Workspace By Handle

### Example


```python
import workspace_sdk
from workspace_sdk.models.workspace_response import WorkspaceResponse
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    handle = 'handle_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Workspace By Handle
        api_response = api_instance.get_workspace_by_handle(handle, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of WorkspacesApi->get_workspace_by_handle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_workspace_by_handle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

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

# **list_workspaces**
> ListWorkspacesResponse list_workspaces(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_workspaces_request=list_workspaces_request)

List Workspaces

### Example


```python
import workspace_sdk
from workspace_sdk.models.list_workspaces_request import ListWorkspacesRequest
from workspace_sdk.models.list_workspaces_response import ListWorkspacesResponse
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)
    list_workspaces_request = workspace_sdk.ListWorkspacesRequest() # ListWorkspacesRequest |  (optional)

    try:
        # List Workspaces
        api_response = api_instance.list_workspaces(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_workspaces_request=list_workspaces_request)
        print("The response of WorkspacesApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 
 **list_workspaces_request** | [**ListWorkspacesRequest**](ListWorkspacesRequest.md)|  | [optional] 

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

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

# **update_workspace**
> WorkspaceResponse update_workspace(workspace_id, workspace_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Update Workspace

### Example


```python
import workspace_sdk
from workspace_sdk.models.workspace_response import WorkspaceResponse
from workspace_sdk.models.workspace_update import WorkspaceUpdate
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    workspace_id = 56 # int | 
    workspace_update = workspace_sdk.WorkspaceUpdate() # WorkspaceUpdate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Update Workspace
        api_response = api_instance.update_workspace(workspace_id, workspace_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of WorkspacesApi->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **workspace_update** | [**WorkspaceUpdate**](WorkspaceUpdate.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

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

# **update_workspace_status**
> WorkspaceResponse update_workspace_status(workspace_id, workspace_status_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Update Workspace Status

### Example


```python
import workspace_sdk
from workspace_sdk.models.workspace_response import WorkspaceResponse
from workspace_sdk.models.workspace_status_update import WorkspaceStatusUpdate
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    workspace_id = 56 # int | 
    workspace_status_update = workspace_sdk.WorkspaceStatusUpdate() # WorkspaceStatusUpdate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Update Workspace Status
        api_response = api_instance.update_workspace_status(workspace_id, workspace_status_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of WorkspacesApi->update_workspace_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **workspace_status_update** | [**WorkspaceStatusUpdate**](WorkspaceStatusUpdate.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

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

# **validate_workspace_exists**
> bool validate_workspace_exists(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Validate Workspace Exists

### Example


```python
import workspace_sdk
from workspace_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = workspace_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with workspace_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspace_sdk.WorkspacesApi(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Validate Workspace Exists
        api_response = api_instance.validate_workspace_exists(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of WorkspacesApi->validate_workspace_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->validate_workspace_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**bool**

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

