# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim

persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_name** | **str** | claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims | 
**read_only** | **bool** | readOnly Will force the ReadOnly setting in VolumeMounts. Default false. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_persistent_volume_claim import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_persistent_volume_claim_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_persistent_volume_claim_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_persistent_volume_claim_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_persistent_volume_claim_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_persistent_volume_claim.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_persistent_volume_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


