# workspace_sdk.FeaturesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch**](FeaturesApi.md#batch) | **POST** /features/batch | Features Batch
[**create_feature**](FeaturesApi.md#create_feature) | **POST** /features/ | Create Feature
[**delete_workspace_feature**](FeaturesApi.md#delete_workspace_feature) | **DELETE** /features/{feature_id} | Delete Feature


# **batch**
> BatchFeaturesResponse batch(batch_features_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Features Batch

### Example


```python
import workspace_sdk
from workspace_sdk.models.batch_features_request import BatchFeaturesRequest
from workspace_sdk.models.batch_features_response import BatchFeaturesResponse
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
    batch_features_request = workspace_sdk.BatchFeaturesRequest() # BatchFeaturesRequest | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Features Batch
        api_response = api_instance.batch(batch_features_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
        print("The response of FeaturesApi->batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_features_request** | [**BatchFeaturesRequest**](BatchFeaturesRequest.md)|  | 
 **x_user_id** | **str**|  | [optional] 
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**BatchFeaturesResponse**](BatchFeaturesResponse.md)

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

# **create_feature**
> FeatureResponse create_feature(create_feature_request, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

Create Feature

### Example


```python
import workspace_sdk
from workspace_sdk.models.create_feature_request import CreateFeatureRequest
from workspace_sdk.models.feature_response import FeatureResponse
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
    x_workspace_id = 56 # int |  (optional)

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
 **x_workspace_id** | **int**|  | [optional] 

### Return type

[**FeatureResponse**](FeatureResponse.md)

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

# **delete_workspace_feature**
> delete_workspace_feature(feature_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)

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
    feature_id = 'feature_id_example' # str | 
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_workspace_id = 56 # int |  (optional)

    try:
        # Delete Feature
        api_instance.delete_workspace_feature(feature_id, x_user_id=x_user_id, x_workspace_id=x_workspace_id)
    except Exception as e:
        print("Exception when calling FeaturesApi->delete_workspace_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**|  | 
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

