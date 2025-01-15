# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpec

The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **List[str]** | accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**data_source** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSource**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSource.md) |  | [optional] 
**data_source_ref** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSourceRef**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSourceRef.md) |  | [optional] 
**resources** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecResources**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecResources.md) |  | [optional] 
**selector** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecSelector**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecSelector.md) |  | [optional] 
**storage_class_name** | **str** | storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 | [optional] 
**volume_attributes_class_name** | **str** | volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it&#39;s not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default). | [optional] 
**volume_mode** | **str** | volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. | [optional] 
**volume_name** | **str** | volumeName is the binding reference to the PersistentVolume backing this claim. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpec from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpec.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpec from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


