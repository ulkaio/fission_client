# IoFissionV1EnvironmentSpecBuilderPodspecDnsConfigOptionsInner

PodDNSConfigOption defines DNS resolver options of a pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_dns_config_options_inner import IoFissionV1EnvironmentSpecBuilderPodspecDnsConfigOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecDnsConfigOptionsInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_dns_config_options_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecDnsConfigOptionsInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecDnsConfigOptionsInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_dns_config_options_inner_dict = io_fission_v1_environment_spec_builder_podspec_dns_config_options_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecDnsConfigOptionsInner from a dict
io_fission_v1_environment_spec_builder_podspec_dns_config_options_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_dns_config_options_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_dns_config_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


