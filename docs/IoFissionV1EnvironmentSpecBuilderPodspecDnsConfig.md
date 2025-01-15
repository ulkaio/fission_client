# IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig

Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nameservers** | **List[str]** | A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed. | [optional] 
**options** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecDnsConfigOptionsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecDnsConfigOptionsInner.md) | A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy. | [optional] 
**searches** | **List[str]** | A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_dns_config import IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig from a JSON string
io_fission_v1_environment_spec_builder_podspec_dns_config_instance = IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_dns_config_dict = io_fission_v1_environment_spec_builder_podspec_dns_config_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig from a dict
io_fission_v1_environment_spec_builder_podspec_dns_config_form_dict = io_fission_v1_environment_spec_builder_podspec_dns_config.from_dict(io_fission_v1_environment_spec_builder_podspec_dns_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


