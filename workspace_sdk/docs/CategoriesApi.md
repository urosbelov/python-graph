# workspace_sdk.CategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_category**](CategoriesApi.md#activate_category) | **POST** /workspaces/categories/{category_id}/activate | Activate Category
[**create_category**](CategoriesApi.md#create_category) | **POST** /workspaces/categories/ | Create Category
[**deactivate_category**](CategoriesApi.md#deactivate_category) | **POST** /workspaces/categories/{category_id}/deactivate | Deactivate Category
[**deprecate_category**](CategoriesApi.md#deprecate_category) | **POST** /workspaces/categories/{category_id}/deprecate | Deprecate Category
[**get_categories_batch**](CategoriesApi.md#get_categories_batch) | **POST** /workspaces/categories/batch | Get Categories Batch
[**get_category**](CategoriesApi.md#get_category) | **GET** /workspaces/categories/{category_id} | Get Category
[**list_categories**](CategoriesApi.md#list_categories) | **POST** /workspaces/categories/list | List Categories


# **activate_category**
> activate_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Activate Category

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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    category_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Activate Category
        api_instance.activate_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling CategoriesApi->activate_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
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

# **create_category**
> Category create_category(create_category_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create Category

### Example


```python
import workspace_sdk
from workspace_sdk.models.category import Category
from workspace_sdk.models.create_category_request import CreateCategoryRequest
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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    create_category_request = workspace_sdk.CreateCategoryRequest() # CreateCategoryRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Create Category
        api_response = api_instance.create_category(create_category_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of CategoriesApi->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->create_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_category_request** | [**CreateCategoryRequest**](CreateCategoryRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**Category**](Category.md)

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

# **deactivate_category**
> deactivate_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Deactivate Category

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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    category_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Deactivate Category
        api_instance.deactivate_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling CategoriesApi->deactivate_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
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

# **deprecate_category**
> deprecate_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Deprecate Category

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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    category_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Deprecate Category
        api_instance.deprecate_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling CategoriesApi->deprecate_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
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

# **get_categories_batch**
> GetCategoriesBatchResponse get_categories_batch(get_categories_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Categories Batch

### Example


```python
import workspace_sdk
from workspace_sdk.models.get_categories_batch_request import GetCategoriesBatchRequest
from workspace_sdk.models.get_categories_batch_response import GetCategoriesBatchResponse
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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    get_categories_batch_request = workspace_sdk.GetCategoriesBatchRequest() # GetCategoriesBatchRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Categories Batch
        api_response = api_instance.get_categories_batch(get_categories_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of CategoriesApi->get_categories_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_categories_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_categories_batch_request** | [**GetCategoriesBatchRequest**](GetCategoriesBatchRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**GetCategoriesBatchResponse**](GetCategoriesBatchResponse.md)

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

# **get_category**
> Category get_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Category

### Example


```python
import workspace_sdk
from workspace_sdk.models.category import Category
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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    category_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Category
        api_response = api_instance.get_category(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of CategoriesApi->get_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**Category**](Category.md)

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
> ListCategoriesResponse list_categories(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_categories_request=list_categories_request)

List Categories

### Example


```python
import workspace_sdk
from workspace_sdk.models.list_categories_request import ListCategoriesRequest
from workspace_sdk.models.list_categories_response import ListCategoriesResponse
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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)
    list_categories_request = workspace_sdk.ListCategoriesRequest() # ListCategoriesRequest |  (optional)

    try:
        # List Categories
        api_response = api_instance.list_categories(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_categories_request=list_categories_request)
        print("The response of CategoriesApi->list_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->list_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 
 **list_categories_request** | [**ListCategoriesRequest**](ListCategoriesRequest.md)|  | [optional] 

### Return type

[**ListCategoriesResponse**](ListCategoriesResponse.md)

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

