# IoFissionV1EnvironmentSpecBuilderPodspecAffinity

If specified, the pod's scheduling constraints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_affinity** | [**IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinity**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinity.md) |  | [optional] 
**pod_affinity** | [**IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinity**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinity.md) |  | [optional] 
**pod_anti_affinity** | [**IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAntiAffinity**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAntiAffinity.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity import IoFissionV1EnvironmentSpecBuilderPodspecAffinity

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinity from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinity.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinity.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_dict = io_fission_v1_environment_spec_builder_podspec_affinity_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinity from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


