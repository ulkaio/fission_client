# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsiSecretRef

secretRef is the CHAP Secret for iSCSI target and initiator authentication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsiSecretRef

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsiSecretRef from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_secret_ref_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsiSecretRef.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsiSecretRef.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_secret_ref_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_secret_ref_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsiSecretRef from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_secret_ref_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_secret_ref.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_secret_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


