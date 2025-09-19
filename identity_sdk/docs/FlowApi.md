# identity_sdk.FlowApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flow**](FlowApi.md#create_flow) | **POST** /flow | Create Flow
[**validate_flow**](FlowApi.md#validate_flow) | **POST** /flow/validate | Validate Flow


# **create_flow**
> FlowResponseBase create_flow(create_flow_request=create_flow_request)

Create Flow

### Example


```python
import identity_sdk
from identity_sdk.models.create_flow_request import CreateFlowRequest
from identity_sdk.models.flow_response_base import FlowResponseBase
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
    api_instance = identity_sdk.FlowApi(api_client)
    create_flow_request = identity_sdk.CreateFlowRequest() # CreateFlowRequest |  (optional)

    try:
        # Create Flow
        api_response = api_instance.create_flow(create_flow_request=create_flow_request)
        print("The response of FlowApi->create_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->create_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_flow_request** | [**CreateFlowRequest**](CreateFlowRequest.md)|  | [optional] 

### Return type

[**FlowResponseBase**](FlowResponseBase.md)

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

# **validate_flow**
> bool validate_flow(validate_flow_request)

Validate Flow

### Example


```python
import identity_sdk
from identity_sdk.models.validate_flow_request import ValidateFlowRequest
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
    api_instance = identity_sdk.FlowApi(api_client)
    validate_flow_request = identity_sdk.ValidateFlowRequest() # ValidateFlowRequest | 

    try:
        # Validate Flow
        api_response = api_instance.validate_flow(validate_flow_request)
        print("The response of FlowApi->validate_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->validate_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_flow_request** | [**ValidateFlowRequest**](ValidateFlowRequest.md)|  | 

### Return type

**bool**

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

