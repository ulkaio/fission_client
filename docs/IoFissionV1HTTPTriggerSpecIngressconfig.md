# IoFissionV1HTTPTriggerSpecIngressconfig

IngressConfig for router to set up Ingress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **object** | Annotations will be added to metadata when creating Ingress. | [optional] 
**host** | **str** | Host is for ingress controller to apply rules. If host is empty or \&quot;*\&quot;, the rule applies to all inbound HTTP traffic. | [optional] 
**path** | **str** | Path is for path matching. The format of path depends on what ingress controller you used. | [optional] 
**tls** | **str** | TLS is for user to specify a Secret that contains TLS key and certificate. The domain name in the key and crt must match the value of Host field. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_http_trigger_spec_ingressconfig import IoFissionV1HTTPTriggerSpecIngressconfig

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1HTTPTriggerSpecIngressconfig from a JSON string
io_fission_v1_http_trigger_spec_ingressconfig_instance = IoFissionV1HTTPTriggerSpecIngressconfig.from_json(json)
# print the JSON string representation of the object
print IoFissionV1HTTPTriggerSpecIngressconfig.to_json()

# convert the object into a dict
io_fission_v1_http_trigger_spec_ingressconfig_dict = io_fission_v1_http_trigger_spec_ingressconfig_instance.to_dict()
# create an instance of IoFissionV1HTTPTriggerSpecIngressconfig from a dict
io_fission_v1_http_trigger_spec_ingressconfig_form_dict = io_fission_v1_http_trigger_spec_ingressconfig.from_dict(io_fission_v1_http_trigger_spec_ingressconfig_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


