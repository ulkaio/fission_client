# IoFissionV1HTTPTriggerSpec

HTTPTriggerSpec is for router to expose user functions at the given URL path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createingress** | **bool** | If CreateIngress is true, router will create an ingress definition. | [optional] 
**functionref** | [**IoFissionV1HTTPTriggerSpecFunctionref**](IoFissionV1HTTPTriggerSpecFunctionref.md) |  | 
**host** | **str** | Deprecated: the original idea of this field is not for setting Ingress. Since we have IngressConfig now, remove Host after couple releases. | [optional] 
**ingressconfig** | [**IoFissionV1HTTPTriggerSpecIngressconfig**](IoFissionV1HTTPTriggerSpecIngressconfig.md) |  | [optional] 
**keep_prefix** | **bool** | When function is exposed with Prefix based path, keepPrefix decides whether to keep or trim prefix in URL while invoking function. | [optional] 
**method** | **str** | Use Methods instead of Method. This field is going to be deprecated in a future release HTTP method to access a function. | [optional] 
**methods** | **List[str]** | HTTP methods to access a function | [optional] 
**prefix** | **str** | Prefix with which functions are exposed. NOTE: Prefix takes precedence over URL/RelativeURL. Note that it does not treat slashes specially (\&quot;/foobar/\&quot; will be matched by the prefix \&quot;/foobar\&quot;). | [optional] 
**relativeurl** | **str** | RelativeURL is the exposed URL for external client to access a function with. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_http_trigger_spec import IoFissionV1HTTPTriggerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1HTTPTriggerSpec from a JSON string
io_fission_v1_http_trigger_spec_instance = IoFissionV1HTTPTriggerSpec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1HTTPTriggerSpec.to_json()

# convert the object into a dict
io_fission_v1_http_trigger_spec_dict = io_fission_v1_http_trigger_spec_instance.to_dict()
# create an instance of IoFissionV1HTTPTriggerSpec from a dict
io_fission_v1_http_trigger_spec_form_dict = io_fission_v1_http_trigger_spec.from_dict(io_fission_v1_http_trigger_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


