# IoFissionV1EnvironmentSpecBuilderPodspecHostAliasesInner

HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostnames** | **List[str]** | Hostnames for the above IP address. | [optional] 
**ip** | **str** | IP address of the host file entry. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_host_aliases_inner import IoFissionV1EnvironmentSpecBuilderPodspecHostAliasesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecHostAliasesInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_host_aliases_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecHostAliasesInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecHostAliasesInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_host_aliases_inner_dict = io_fission_v1_environment_spec_builder_podspec_host_aliases_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecHostAliasesInner from a dict
io_fission_v1_environment_spec_builder_podspec_host_aliases_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_host_aliases_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_host_aliases_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


