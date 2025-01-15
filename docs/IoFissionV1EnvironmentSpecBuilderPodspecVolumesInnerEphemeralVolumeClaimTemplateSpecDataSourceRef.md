# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSourceRef

dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef   allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef   preserves all values, and generates an error if a disallowed value is   specified. * While dataSource only allows local objects, dataSourceRef allows objects   in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. | [optional] 
**kind** | **str** | Kind is the type of resource being referenced | 
**name** | **str** | Name is the name of resource being referenced | 
**namespace** | **str** | Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace&#39;s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSourceRef

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSourceRef from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_ref_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSourceRef.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSourceRef.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_ref_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_ref_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSourceRef from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_ref_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_ref.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


