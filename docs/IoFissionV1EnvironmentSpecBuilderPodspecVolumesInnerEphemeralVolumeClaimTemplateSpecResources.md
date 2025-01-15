# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecResources

resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | **Dict[str, object]** | Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 
**requests** | **Dict[str, object]** | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_resources import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecResources

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecResources from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_resources_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecResources.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecResources.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_resources_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_resources_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecResources from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_resources_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_resources.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


