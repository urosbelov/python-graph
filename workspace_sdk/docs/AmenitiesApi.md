# workspace_sdk.AmenitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_amenities**](AmenitiesApi.md#batch_amenities) | **POST** /api/v1/amenities/batch | Batch Amenities
[**create_amenity**](AmenitiesApi.md#create_amenity) | **POST** /api/v1/amenities/ | Create Amenity
[**get_amenity**](AmenitiesApi.md#get_amenity) | **GET** /api/v1/amenities/{amenity_id} | Get Amenity
[**list_amenities**](AmenitiesApi.md#list_amenities) | **POST** /api/v1/amenities/list | List Amenities
[**update_amenity**](AmenitiesApi.md#update_amenity) | **PUT** /api/v1/amenities/{amenity_id} | Update Amenity


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
    api_instance = workspace_sdk.AmenitiesApi(api_client)
    batch_amenities_request = workspace_sdk.BatchAmenitiesRequest() # BatchAmenitiesRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Batch Amenities
        api_response = api_instance.batch_amenities(batch_amenities_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of AmenitiesApi->batch_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->batch_amenities: %s\n" % e)
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
    api_instance = workspace_sdk.AmenitiesApi(api_client)
    amenity_create = workspace_sdk.AmenityCreate() # AmenityCreate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Create Amenity
        api_response = api_instance.create_amenity(amenity_create, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of AmenitiesApi->create_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->create_amenity: %s\n" % e)
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
    api_instance = workspace_sdk.AmenitiesApi(api_client)
    amenity_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Get Amenity
        api_response = api_instance.get_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of AmenitiesApi->get_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->get_amenity: %s\n" % e)
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
    api_instance = workspace_sdk.AmenitiesApi(api_client)
    list_amenities_request = workspace_sdk.ListAmenitiesRequest() # ListAmenitiesRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # List Amenities
        api_response = api_instance.list_amenities(list_amenities_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of AmenitiesApi->list_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->list_amenities: %s\n" % e)
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
    api_instance = workspace_sdk.AmenitiesApi(api_client)
    amenity_id = 56 # int | 
    amenity_update = workspace_sdk.AmenityUpdate() # AmenityUpdate | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Update Amenity
        api_response = api_instance.update_amenity(amenity_id, amenity_update, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of AmenitiesApi->update_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->update_amenity: %s\n" % e)
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

