# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSource

dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. | [optional] 
**kind** | **str** | Kind is the type of resource being referenced | 
**name** | **str** | Name is the name of resource being referenced | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSource

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSource from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSource.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSource.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSource from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


