# workspace_sdk.V1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_activate_put**](V1Api.md#activate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_activate_put) | **PUT** /api/v1/categories/{category_id}/amenities/{amenity_id}/activate | Activate Amenity In Category
[**activate_workspace**](V1Api.md#activate_workspace) | **PUT** /api/v1/workspaces/{workspace_id}/activate | Activate Workspace
[**add_amenity_to_category**](V1Api.md#add_amenity_to_category) | **POST** /api/v1/categories/{category_id}/amenities/{amenity_id} | Add Amenity To Category
[**add_amenity_to_workspace**](V1Api.md#add_amenity_to_workspace) | **POST** /api/v1/workspaces/{workspace_id}/amenities/{amenity_id} | Add Amenity To Workspace
[**batch_amenities**](V1Api.md#batch_amenities) | **POST** /api/v1/amenities/batch | Batch Amenities
[**batch_categories**](V1Api.md#batch_categories) | **POST** /api/v1/categories/batch | Batch Categories
[**batch_workspaces**](V1Api.md#batch_workspaces) | **POST** /api/v1/workspaces/batch | Get Workspaces By Ids
[**check_amenities_enabled**](V1Api.md#check_amenities_enabled) | **POST** /api/v1/workspaces/amenities/check | Check Amenities Enabled
[**create_amenity**](V1Api.md#create_amenity) | **POST** /api/v1/amenities/ | Create Amenity
[**create_category**](V1Api.md#create_category) | **POST** /api/v1/categories/ | Create Category
[**create_workspace**](V1Api.md#create_workspace) | **POST** /api/v1/workspaces/ | Create Workspace
[**deactivate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deactivate_put**](V1Api.md#deactivate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deactivate_put) | **PUT** /api/v1/categories/{category_id}/amenities/{amenity_id}/deactivate | Deactivate Amenity In Category
[**deactivate_workspace**](V1Api.md#deactivate_workspace) | **PUT** /api/v1/workspaces/{workspace_id}/deactivate | Deactivate Workspace
[**deprecate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deprecate_put**](V1Api.md#deprecate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deprecate_put) | **PUT** /api/v1/categories/{category_id}/amenities/{amenity_id}/deprecate | Deprecate Amenity In Category
[**get_amenity**](V1Api.md#get_amenity) | **GET** /api/v1/amenities/{amenity_id} | Get Amenity
[**get_category**](V1Api.md#get_category) | **GET** /api/v1/categories/{category_id} | Get Category
[**get_workspace**](V1Api.md#get_workspace) | **GET** /api/v1/workspaces/{workspace_id} | Get Workspace
[**get_workspace_by_handle**](V1Api.md#get_workspace_by_handle) | **GET** /api/v1/workspaces/handle/{handle} | Get Workspace By Handle
[**list_amenities**](V1Api.md#list_amenities) | **POST** /api/v1/amenities/list | List Amenities
[**list_amenities_in_category_api_v1_categories_category_id_amenities_get**](V1Api.md#list_amenities_in_category_api_v1_categories_category_id_amenities_get) | **GET** /api/v1/categories/{category_id}/amenities | List Amenities In Category
[**list_categories**](V1Api.md#list_categories) | **GET** /api/v1/categories/list | List Categories
[**remove_amenity_from_workspace**](V1Api.md#remove_amenity_from_workspace) | **POST** /api/v1/workspaces/{workspace_id}/amenities/{amenity_id}/remove | Remove Amenity From Workspace
[**suspend_workspace**](V1Api.md#suspend_workspace) | **PUT** /api/v1/workspaces/{workspace_id}/suspend | Suspend Workspace
[**update_amenity**](V1Api.md#update_amenity) | **PUT** /api/v1/amenities/{amenity_id} | Update Amenity
[**update_category**](V1Api.md#update_category) | **PUT** /api/v1/categories/{category_id} | Update Category
[**update_workspace**](V1Api.md#update_workspace) | **PUT** /api/v1/workspaces/{workspace_id} | Update Workspace
[**validate_workspace_exists**](V1Api.md#validate_workspace_exists) | **GET** /api/v1/workspaces/{workspace_id}/exist | Validate Workspace Exists


# **activate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_activate_put**
> object activate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_activate_put(category_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Activate Amenity In Category

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
    api_instance = workspace_sdk.V1Api(api_client)
    category_id = 56 # int | 
    amenity_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Activate Amenity In Category
        api_response = api_instance.activate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_activate_put(category_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->activate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_activate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->activate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_activate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **amenity_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **activate_workspace**
> activate_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Activate Workspace

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
    api_instance = workspace_sdk.V1Api(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Activate Workspace
        api_instance.activate_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling V1Api->activate_workspace: %s\n" % e)
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

# **add_amenity_to_category**
> object add_amenity_to_category(category_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Add Amenity To Category

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
    api_instance = workspace_sdk.V1Api(api_client)
    category_id = 56 # int | 
    amenity_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Add Amenity To Category
        api_response = api_instance.add_amenity_to_category(category_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->add_amenity_to_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->add_amenity_to_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **amenity_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **add_amenity_to_workspace**
> add_amenity_to_workspace(workspace_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Add Amenity To Workspace

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
    api_instance = workspace_sdk.V1Api(api_client)
    workspace_id = 56 # int | 
    amenity_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Add Amenity To Workspace
        api_instance.add_amenity_to_workspace(workspace_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling V1Api->add_amenity_to_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **amenity_id** | **int**|  | 
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

# **batch_amenities**
> object batch_amenities(batch_amenities_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Batch Amenities

### Example


```python
import workspace_sdk
from workspace_sdk.models.batch_amenities_request import BatchAmenitiesRequest
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
    api_instance = workspace_sdk.V1Api(api_client)
    batch_amenities_request = workspace_sdk.BatchAmenitiesRequest() # BatchAmenitiesRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Batch Amenities
        api_response = api_instance.batch_amenities(batch_amenities_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->batch_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->batch_amenities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_amenities_request** | [**BatchAmenitiesRequest**](BatchAmenitiesRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **batch_categories**
> object batch_categories(batch_categories_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Batch Categories

### Example


```python
import workspace_sdk
from workspace_sdk.models.batch_categories_request import BatchCategoriesRequest
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
    api_instance = workspace_sdk.V1Api(api_client)
    batch_categories_request = workspace_sdk.BatchCategoriesRequest() # BatchCategoriesRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Batch Categories
        api_response = api_instance.batch_categories(batch_categories_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->batch_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->batch_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_categories_request** | [**BatchCategoriesRequest**](BatchCategoriesRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **batch_workspaces**
> List[WorkspaceResponse] batch_workspaces(batch_workspaces_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Workspaces By Ids

### Example


```python
import workspace_sdk
from workspace_sdk.models.batch_workspaces_request import BatchWorkspacesRequest
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
    api_instance = workspace_sdk.V1Api(api_client)
    batch_workspaces_request = workspace_sdk.BatchWorkspacesRequest() # BatchWorkspacesRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Workspaces By Ids
        api_response = api_instance.batch_workspaces(batch_workspaces_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->batch_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->batch_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_workspaces_request** | [**BatchWorkspacesRequest**](BatchWorkspacesRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

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

# **check_amenities_enabled**
> Dict[str, bool] check_amenities_enabled(batch_amenity_check_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Check Amenities Enabled

### Example


```python
import workspace_sdk
from workspace_sdk.models.batch_amenity_check_request import BatchAmenityCheckRequest
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
    api_instance = workspace_sdk.V1Api(api_client)
    batch_amenity_check_request = workspace_sdk.BatchAmenityCheckRequest() # BatchAmenityCheckRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Check Amenities Enabled
        api_response = api_instance.check_amenities_enabled(batch_amenity_check_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->check_amenities_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->check_amenities_enabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_amenity_check_request** | [**BatchAmenityCheckRequest**](BatchAmenityCheckRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**Dict[str, bool]**

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

# **create_amenity**
> object create_amenity(amenity_create, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create Amenity

### Example


```python
import workspace_sdk
from workspace_sdk.models.amenity_create import AmenityCreate
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
    api_instance = workspace_sdk.V1Api(api_client)
    amenity_create = workspace_sdk.AmenityCreate() # AmenityCreate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Create Amenity
        api_response = api_instance.create_amenity(amenity_create, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->create_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amenity_create** | [**AmenityCreate**](AmenityCreate.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **create_category**
> object create_category(category_create, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create Category

### Example


```python
import workspace_sdk
from workspace_sdk.models.category_create import CategoryCreate
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
    api_instance = workspace_sdk.V1Api(api_client)
    category_create = workspace_sdk.CategoryCreate() # CategoryCreate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Create Category
        api_response = api_instance.create_category(category_create, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_create** | [**CategoryCreate**](CategoryCreate.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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
    api_instance = workspace_sdk.V1Api(api_client)
    workspace_create = workspace_sdk.WorkspaceCreate() # WorkspaceCreate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Create Workspace
        api_response = api_instance.create_workspace(workspace_create, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_workspace: %s\n" % e)
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

# **deactivate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deactivate_put**
> object deactivate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deactivate_put(category_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Deactivate Amenity In Category

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
    api_instance = workspace_sdk.V1Api(api_client)
    category_id = 56 # int | 
    amenity_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Deactivate Amenity In Category
        api_response = api_instance.deactivate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deactivate_put(category_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->deactivate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deactivate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->deactivate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deactivate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **amenity_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **deactivate_workspace**
> deactivate_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Deactivate Workspace

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
    api_instance = workspace_sdk.V1Api(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Deactivate Workspace
        api_instance.deactivate_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling V1Api->deactivate_workspace: %s\n" % e)
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

# **deprecate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deprecate_put**
> object deprecate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deprecate_put(category_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Deprecate Amenity In Category

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
    api_instance = workspace_sdk.V1Api(api_client)
    category_id = 56 # int | 
    amenity_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Deprecate Amenity In Category
        api_response = api_instance.deprecate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deprecate_put(category_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->deprecate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deprecate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->deprecate_amenity_in_category_api_v1_categories_category_id_amenities_amenity_id_deprecate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **amenity_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **get_amenity**
> object get_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Amenity

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
    api_instance = workspace_sdk.V1Api(api_client)
    amenity_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Amenity
        api_response = api_instance.get_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->get_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amenity_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **get_category**
> object get_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Category

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
    api_instance = workspace_sdk.V1Api(api_client)
    category_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Category
        api_response = api_instance.get_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->get_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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
    api_instance = workspace_sdk.V1Api(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Workspace
        api_response = api_instance.get_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_workspace: %s\n" % e)
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
    api_instance = workspace_sdk.V1Api(api_client)
    handle = 'handle_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Workspace By Handle
        api_response = api_instance.get_workspace_by_handle(handle, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->get_workspace_by_handle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_workspace_by_handle: %s\n" % e)
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

# **list_amenities**
> object list_amenities(list_amenities_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

List Amenities

### Example


```python
import workspace_sdk
from workspace_sdk.models.list_amenities_request import ListAmenitiesRequest
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
    api_instance = workspace_sdk.V1Api(api_client)
    list_amenities_request = workspace_sdk.ListAmenitiesRequest() # ListAmenitiesRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # List Amenities
        api_response = api_instance.list_amenities(list_amenities_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->list_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_amenities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_amenities_request** | [**ListAmenitiesRequest**](ListAmenitiesRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **list_amenities_in_category_api_v1_categories_category_id_amenities_get**
> object list_amenities_in_category_api_v1_categories_category_id_amenities_get(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

List Amenities In Category

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
    api_instance = workspace_sdk.V1Api(api_client)
    category_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # List Amenities In Category
        api_response = api_instance.list_amenities_in_category_api_v1_categories_category_id_amenities_get(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->list_amenities_in_category_api_v1_categories_category_id_amenities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_amenities_in_category_api_v1_categories_category_id_amenities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **list_categories**
> object list_categories(x_user_id=x_user_id, x_workspace_id=x_workspace_id)

List Categories

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
    api_instance = workspace_sdk.V1Api(api_client)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # List Categories
        api_response = api_instance.list_categories(x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->list_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **remove_amenity_from_workspace**
> remove_amenity_from_workspace(workspace_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Remove Amenity From Workspace

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
    api_instance = workspace_sdk.V1Api(api_client)
    workspace_id = 56 # int | 
    amenity_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Remove Amenity From Workspace
        api_instance.remove_amenity_from_workspace(workspace_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling V1Api->remove_amenity_from_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **amenity_id** | **int**|  | 
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

# **suspend_workspace**
> suspend_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Suspend Workspace

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
    api_instance = workspace_sdk.V1Api(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Suspend Workspace
        api_instance.suspend_workspace(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling V1Api->suspend_workspace: %s\n" % e)
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

# **update_amenity**
> object update_amenity(amenity_id, amenity_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Update Amenity

### Example


```python
import workspace_sdk
from workspace_sdk.models.amenity_update import AmenityUpdate
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
    api_instance = workspace_sdk.V1Api(api_client)
    amenity_id = 56 # int | 
    amenity_update = workspace_sdk.AmenityUpdate() # AmenityUpdate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Update Amenity
        api_response = api_instance.update_amenity(amenity_id, amenity_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->update_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amenity_id** | **int**|  | 
 **amenity_update** | [**AmenityUpdate**](AmenityUpdate.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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

# **update_category**
> object update_category(category_id, category_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Update Category

### Example


```python
import workspace_sdk
from workspace_sdk.models.category_update import CategoryUpdate
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
    api_instance = workspace_sdk.V1Api(api_client)
    category_id = 56 # int | 
    category_update = workspace_sdk.CategoryUpdate() # CategoryUpdate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Update Category
        api_response = api_instance.update_category(category_id, category_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **category_update** | [**CategoryUpdate**](CategoryUpdate.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

**object**

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
    api_instance = workspace_sdk.V1Api(api_client)
    workspace_id = 56 # int | 
    workspace_update = workspace_sdk.WorkspaceUpdate() # WorkspaceUpdate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Update Workspace
        api_response = api_instance.update_workspace(workspace_id, workspace_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_workspace: %s\n" % e)
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
    api_instance = workspace_sdk.V1Api(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Validate Workspace Exists
        api_response = api_instance.validate_workspace_exists(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of V1Api->validate_workspace_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->validate_workspace_exists: %s\n" % e)
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

