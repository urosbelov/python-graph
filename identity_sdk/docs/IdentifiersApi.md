# identity_sdk.IdentifiersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identifier**](IdentifiersApi.md#create_identifier) | **POST** /users/identifiers | Create Identifier
[**delete_identifier**](IdentifiersApi.md#delete_identifier) | **DELETE** /users/identifiers/{identifier_id} | Delete Identifier
[**set_default_identifier**](IdentifiersApi.md#set_default_identifier) | **POST** /users/identifiers/default/{identifier_id} | Set Default Identifier
[**validate_identifier_otp**](IdentifiersApi.md#validate_identifier_otp) | **POST** /users/identifiers/validate-otp | Validate Identifier Otp


# **create_identifier**
> IdentifierResponse create_identifier(create_identifier_request)

Create Identifier

### Example


```python
import identity_sdk
from identity_sdk.models.create_identifier_request import CreateIdentifierRequest
from identity_sdk.models.identifier_response import IdentifierResponse
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
    api_instance = identity_sdk.IdentifiersApi(api_client)
    create_identifier_request = identity_sdk.CreateIdentifierRequest() # CreateIdentifierRequest | 

    try:
        # Create Identifier
        api_response = api_instance.create_identifier(create_identifier_request)
        print("The response of IdentifiersApi->create_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentifiersApi->create_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_identifier_request** | [**CreateIdentifierRequest**](CreateIdentifierRequest.md)|  | 

### Return type

[**IdentifierResponse**](IdentifierResponse.md)

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

# **delete_identifier**
> delete_identifier(identifier_id)

Delete Identifier

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
    api_instance = identity_sdk.IdentifiersApi(api_client)
    identifier_id = 'identifier_id_example' # str | 

    try:
        # Delete Identifier
        api_instance.delete_identifier(identifier_id)
    except Exception as e:
        print("Exception when calling IdentifiersApi->delete_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_id** | **str**|  | 

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

# **set_default_identifier**
> IdentifierResponse set_default_identifier(identifier_id)

Set Default Identifier

### Example


```python
import identity_sdk
from identity_sdk.models.identifier_response import IdentifierResponse
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
    api_instance = identity_sdk.IdentifiersApi(api_client)
    identifier_id = 'identifier_id_example' # str | 

    try:
        # Set Default Identifier
        api_response = api_instance.set_default_identifier(identifier_id)
        print("The response of IdentifiersApi->set_default_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentifiersApi->set_default_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_id** | **str**|  | 

### Return type

[**IdentifierResponse**](IdentifierResponse.md)

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

# **validate_identifier_otp**
> validate_identifier_otp(validate_identifier_otp_request)

Validate Identifier Otp

### Example


```python
import identity_sdk
from identity_sdk.models.validate_identifier_otp_request import ValidateIdentifierOTPRequest
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
    api_instance = identity_sdk.IdentifiersApi(api_client)
    validate_identifier_otp_request = identity_sdk.ValidateIdentifierOTPRequest() # ValidateIdentifierOTPRequest | 

    try:
        # Validate Identifier Otp
        api_instance.validate_identifier_otp(validate_identifier_otp_request)
    except Exception as e:
        print("Exception when calling IdentifiersApi->validate_identifier_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_identifier_otp_request** | [**ValidateIdentifierOTPRequest**](ValidateIdentifierOTPRequest.md)|  | 

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

