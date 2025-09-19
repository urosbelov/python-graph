# identity_sdk.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_profile**](AuthApi.md#create_profile) | **POST** /auth/create-profile | Create Profile
[**login**](AuthApi.md#login) | **POST** /auth/login | Login
[**validate_identifier**](AuthApi.md#validate_identifier) | **POST** /auth/identifier/validate | Validate Identifier
[**verify_identifier**](AuthApi.md#verify_identifier) | **POST** /auth/verify-identifier | Verify Identifier


# **create_profile**
> create_profile(create_profile_request)

Create Profile

### Example


```python
import identity_sdk
from identity_sdk.models.create_profile_request import CreateProfileRequest
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
    api_instance = identity_sdk.AuthApi(api_client)
    create_profile_request = identity_sdk.CreateProfileRequest() # CreateProfileRequest | 

    try:
        # Create Profile
        api_instance.create_profile(create_profile_request)
    except Exception as e:
        print("Exception when calling AuthApi->create_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_profile_request** | [**CreateProfileRequest**](CreateProfileRequest.md)|  | 

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

# **login**
> AuthenticatedResponse login(login_request)

Login

### Example


```python
import identity_sdk
from identity_sdk.models.authenticated_response import AuthenticatedResponse
from identity_sdk.models.login_request import LoginRequest
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
    api_instance = identity_sdk.AuthApi(api_client)
    login_request = identity_sdk.LoginRequest() # LoginRequest | 

    try:
        # Login
        api_response = api_instance.login(login_request)
        print("The response of AuthApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**AuthenticatedResponse**](AuthenticatedResponse.md)

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

# **validate_identifier**
> bool validate_identifier(validate_identifier_request=validate_identifier_request)

Validate Identifier

### Example


```python
import identity_sdk
from identity_sdk.models.validate_identifier_request import ValidateIdentifierRequest
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
    api_instance = identity_sdk.AuthApi(api_client)
    validate_identifier_request = identity_sdk.ValidateIdentifierRequest() # ValidateIdentifierRequest |  (optional)

    try:
        # Validate Identifier
        api_response = api_instance.validate_identifier(validate_identifier_request=validate_identifier_request)
        print("The response of AuthApi->validate_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->validate_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_identifier_request** | [**ValidateIdentifierRequest**](ValidateIdentifierRequest.md)|  | [optional] 

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

# **verify_identifier**
> AuthenticatedResponse verify_identifier(verify_identifier_request)

Verify Identifier

### Example


```python
import identity_sdk
from identity_sdk.models.authenticated_response import AuthenticatedResponse
from identity_sdk.models.verify_identifier_request import VerifyIdentifierRequest
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
    api_instance = identity_sdk.AuthApi(api_client)
    verify_identifier_request = identity_sdk.VerifyIdentifierRequest() # VerifyIdentifierRequest | 

    try:
        # Verify Identifier
        api_response = api_instance.verify_identifier(verify_identifier_request)
        print("The response of AuthApi->verify_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->verify_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_identifier_request** | [**VerifyIdentifierRequest**](VerifyIdentifierRequest.md)|  | 

### Return type

[**AuthenticatedResponse**](AuthenticatedResponse.md)

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

