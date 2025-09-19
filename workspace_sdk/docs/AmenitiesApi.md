# workspace_sdk.AmenitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_amenity**](AmenitiesApi.md#activate_amenity) | **POST** /workspaces/amenities/{amenity_id}/activate | Activate Amenity
[**create_amenity**](AmenitiesApi.md#create_amenity) | **POST** /workspaces/amenities/ | Create Amenity
[**deactivate_amenity**](AmenitiesApi.md#deactivate_amenity) | **POST** /workspaces/amenities/{amenity_id}/deactivate | Deactivate Amenity
[**deprecate_amenity**](AmenitiesApi.md#deprecate_amenity) | **POST** /workspaces/amenities/{amenity_id}/deprecate | Deprecate Amenity
[**get_amenities_batch**](AmenitiesApi.md#get_amenities_batch) | **POST** /workspaces/amenities/batch | Get Amenities Batch
[**get_amenity**](AmenitiesApi.md#get_amenity) | **GET** /workspaces/amenities/{amenity_id} | Get Amenity
[**list_amenities**](AmenitiesApi.md#list_amenities) | **POST** /workspaces/amenities/list | List Amenities


# **activate_amenity**
> activate_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Activate Amenity

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
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Activate Amenity
        api_instance.activate_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling AmenitiesApi->activate_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amenity_id** | **int**|  | 
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

# **create_amenity**
> Amenity create_amenity(create_amenity_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create Amenity

### Example


```python
import workspace_sdk
from workspace_sdk.models.amenity import Amenity
from workspace_sdk.models.create_amenity_request import CreateAmenityRequest
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
    create_amenity_request = workspace_sdk.CreateAmenityRequest() # CreateAmenityRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Create Amenity
        api_response = api_instance.create_amenity(create_amenity_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of AmenitiesApi->create_amenity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->create_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_amenity_request** | [**CreateAmenityRequest**](CreateAmenityRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**Amenity**](Amenity.md)

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

# **deactivate_amenity**
> deactivate_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Deactivate Amenity

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
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Deactivate Amenity
        api_instance.deactivate_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling AmenitiesApi->deactivate_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amenity_id** | **int**|  | 
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

# **deprecate_amenity**
> deprecate_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Deprecate Amenity

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
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Deprecate Amenity
        api_instance.deprecate_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling AmenitiesApi->deprecate_amenity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amenity_id** | **int**|  | 
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

# **get_amenities_batch**
> GetAmenitiesBatchResponse get_amenities_batch(get_amenities_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Amenities Batch

### Example


```python
import workspace_sdk
from workspace_sdk.models.get_amenities_batch_request import GetAmenitiesBatchRequest
from workspace_sdk.models.get_amenities_batch_response import GetAmenitiesBatchResponse
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
    get_amenities_batch_request = workspace_sdk.GetAmenitiesBatchRequest() # GetAmenitiesBatchRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Amenities Batch
        api_response = api_instance.get_amenities_batch(get_amenities_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of AmenitiesApi->get_amenities_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->get_amenities_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_amenities_batch_request** | [**GetAmenitiesBatchRequest**](GetAmenitiesBatchRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**GetAmenitiesBatchResponse**](GetAmenitiesBatchResponse.md)

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
> Amenity get_amenity(amenity_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Amenity

### Example


```python
import workspace_sdk
from workspace_sdk.models.amenity import Amenity
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
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

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
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**Amenity**](Amenity.md)

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
> ListAmenitiesResponse list_amenities(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_amenities_request=list_amenities_request)

List Amenities

### Example


```python
import workspace_sdk
from workspace_sdk.models.list_amenities_request import ListAmenitiesRequest
from workspace_sdk.models.list_amenities_response import ListAmenitiesResponse
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
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)
    list_amenities_request = workspace_sdk.ListAmenitiesRequest() # ListAmenitiesRequest |  (optional)

    try:
        # List Amenities
        api_response = api_instance.list_amenities(x_user_id=x_user_id, x_workspace_id=x_workspace_id, list_amenities_request=list_amenities_request)
        print("The response of AmenitiesApi->list_amenities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmenitiesApi->list_amenities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 
 **list_amenities_request** | [**ListAmenitiesRequest**](ListAmenitiesRequest.md)|  | [optional] 

### Return type

[**ListAmenitiesResponse**](ListAmenitiesResponse.md)

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

