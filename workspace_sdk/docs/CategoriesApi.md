# workspace_sdk.CategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_amenity_to_category**](CategoriesApi.md#add_amenity_to_category) | **POST** /categories/{category_id}/amenities/{amenity_id} | Add Amenity To Category
[**batch_categories**](CategoriesApi.md#batch_categories) | **POST** /categories/batch | Batch Categories
[**create_category**](CategoriesApi.md#create_category) | **POST** /categories/ | Create Category
[**get_category**](CategoriesApi.md#get_category) | **GET** /categories/{category_id} | Get Category
[**list_amenities_in_category_categories_category_id_amenities_get**](CategoriesApi.md#list_amenities_in_category_categories_category_id_amenities_get) | **GET** /categories/{category_id}/amenities | List Amenities In Category
[**list_categories**](CategoriesApi.md#list_categories) | **POST** /categories/list | List Categories
[**update_amenity_in_category**](CategoriesApi.md#update_amenity_in_category) | **PUT** /categories/{category_id}/amenities/{amenity_id} | Update Amenity In Category
[**update_category**](CategoriesApi.md#update_category) | **PUT** /categories/{category_id} | Update Category


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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    category_id = 56 # int | 
    amenity_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Add Amenity To Category
        api_response = api_instance.add_amenity_to_category(category_id, amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of CategoriesApi->add_amenity_to_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->add_amenity_to_category: %s\n" % e)
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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    batch_categories_request = workspace_sdk.BatchCategoriesRequest() # BatchCategoriesRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Batch Categories
        api_response = api_instance.batch_categories(batch_categories_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of CategoriesApi->batch_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->batch_categories: %s\n" % e)
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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    category_create = workspace_sdk.CategoryCreate() # CategoryCreate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Create Category
        api_response = api_instance.create_category(category_create, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of CategoriesApi->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->create_category: %s\n" % e)
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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    category_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

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

# **list_amenities_in_category_categories_category_id_amenities_get**
> object list_amenities_in_category_categories_category_id_amenities_get(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    category_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # List Amenities In Category
        api_response = api_instance.list_amenities_in_category_categories_category_id_amenities_get(category_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of CategoriesApi->list_amenities_in_category_categories_category_id_amenities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->list_amenities_in_category_categories_category_id_amenities_get: %s\n" % e)
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
> object list_categories(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_categories_request=list_categories_request)

List Categories

### Example


```python
import workspace_sdk
from workspace_sdk.models.list_categories_request import ListCategoriesRequest
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
    x_workspace_id = 56 # int |  (optional)
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
 **x_workspace_id** | **int**|  | [optional] 
 **list_categories_request** | [**ListCategoriesRequest**](ListCategoriesRequest.md)|  | [optional] 

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

# **update_amenity_in_category**
> update_amenity_in_category(category_id, amenity_id, update_category_amenity, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Update Amenity In Category

### Example


```python
import workspace_sdk
from workspace_sdk.models.update_category_amenity import UpdateCategoryAmenity
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
    amenity_id = 56 # int | 
    update_category_amenity = workspace_sdk.UpdateCategoryAmenity() # UpdateCategoryAmenity | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Update Amenity In Category
        api_instance.update_amenity_in_category(category_id, amenity_id, update_category_amenity, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling CategoriesApi->update_amenity_in_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **amenity_id** | **int**|  | 
 **update_category_amenity** | [**UpdateCategoryAmenity**](UpdateCategoryAmenity.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
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
    api_instance = workspace_sdk.CategoriesApi(api_client)
    category_id = 56 # int | 
    category_update = workspace_sdk.CategoryUpdate() # CategoryUpdate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Update Category
        api_response = api_instance.update_category(category_id, category_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of CategoriesApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->update_category: %s\n" % e)
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

