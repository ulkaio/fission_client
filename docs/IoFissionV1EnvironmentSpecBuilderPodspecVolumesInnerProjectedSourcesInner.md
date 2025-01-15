# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInner

Projection that may be projected along with other supported volume types. Exactly one of these fields must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_trust_bundle** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundle**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundle.md) |  | [optional] 
**config_map** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerConfigMap**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerConfigMap.md) |  | [optional] 
**downward_api** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerDownwardAPI**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerDownwardAPI.md) |  | [optional] 
**secret** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerSecret**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerSecret.md) |  | [optional] 
**service_account_token** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInner from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


