# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIOSecretRef

secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIOSecretRef

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIOSecretRef from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_secret_ref_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIOSecretRef.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIOSecretRef.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_secret_ref_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_secret_ref_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIOSecretRef from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_secret_ref_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_secret_ref.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_secret_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


