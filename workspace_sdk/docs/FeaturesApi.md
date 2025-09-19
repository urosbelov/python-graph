# workspace_sdk.FeaturesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_feature**](FeaturesApi.md#activate_feature) | **POST** /workspaces/features/{workspace_id}/activate | Activate Feature
[**create_feature**](FeaturesApi.md#create_feature) | **POST** /workspaces/features | Create Feature
[**deactivate_feature**](FeaturesApi.md#deactivate_feature) | **POST** /workspaces/features/{workspace_id}/deactivate | Deactivate Feature
[**delete_feature**](FeaturesApi.md#delete_feature) | **DELETE** /workspaces/features/{workspace_id}/{feature_id} | Delete Feature
[**get_features_batch**](FeaturesApi.md#get_features_batch) | **POST** /workspaces/features/batch | Get Features Batch
[**get_workspace_features**](FeaturesApi.md#get_workspace_features) | **GET** /workspaces/features/{workspace_id} | Get Workspace Features


# **activate_feature**
> object activate_feature(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Activate Feature

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
    api_instance = workspace_sdk.FeaturesApi(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Activate Feature
        api_response = api_instance.activate_feature(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of FeaturesApi->activate_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->activate_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

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

# **create_feature**
> Feature create_feature(create_feature_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create Feature

### Example


```python
import workspace_sdk
from workspace_sdk.models.create_feature_request import CreateFeatureRequest
from workspace_sdk.models.feature import Feature
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
    api_instance = workspace_sdk.FeaturesApi(api_client)
    create_feature_request = workspace_sdk.CreateFeatureRequest() # CreateFeatureRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Create Feature
        api_response = api_instance.create_feature(create_feature_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of FeaturesApi->create_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->create_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_feature_request** | [**CreateFeatureRequest**](CreateFeatureRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**Feature**](Feature.md)

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

# **deactivate_feature**
> object deactivate_feature(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Deactivate Feature

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
    api_instance = workspace_sdk.FeaturesApi(api_client)
    workspace_id = 56 # int | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Deactivate Feature
        api_response = api_instance.deactivate_feature(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of FeaturesApi->deactivate_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->deactivate_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

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

# **delete_feature**
> object delete_feature(workspace_id, feature_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Delete Feature

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
    api_instance = workspace_sdk.FeaturesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    feature_id = 'feature_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Delete Feature
        api_response = api_instance.delete_feature(workspace_id, feature_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of FeaturesApi->delete_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->delete_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **feature_id** | **str**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

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

# **get_features_batch**
> GetFeaturesBatchResponse get_features_batch(get_features_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Features Batch

### Example


```python
import workspace_sdk
from workspace_sdk.models.get_features_batch_request import GetFeaturesBatchRequest
from workspace_sdk.models.get_features_batch_response import GetFeaturesBatchResponse
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
    api_instance = workspace_sdk.FeaturesApi(api_client)
    get_features_batch_request = workspace_sdk.GetFeaturesBatchRequest() # GetFeaturesBatchRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Features Batch
        api_response = api_instance.get_features_batch(get_features_batch_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of FeaturesApi->get_features_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->get_features_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_features_batch_request** | [**GetFeaturesBatchRequest**](GetFeaturesBatchRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**GetFeaturesBatchResponse**](GetFeaturesBatchResponse.md)

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

# **get_workspace_features**
> ListWorkspaceFeaturesResponse get_workspace_features(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Get Workspace Features

### Example


```python
import workspace_sdk
from workspace_sdk.models.list_workspace_features_response import ListWorkspaceFeaturesResponse
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
    api_instance = workspace_sdk.FeaturesApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 'x_workspace_id_example' # str |  (optional)

    try:
        # Get Workspace Features
        api_response = api_instance.get_workspace_features(workspace_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of FeaturesApi->get_workspace_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->get_workspace_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **str**|  | [optional] 

### Return type

[**ListWorkspaceFeaturesResponse**](ListWorkspaceFeaturesResponse.md)

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

