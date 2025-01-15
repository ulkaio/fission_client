# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken

serviceAccountToken is information about the serviceAccountToken data to project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver. | [optional] 
**expiration_seconds** | **int** | expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes. | [optional] 
**path** | **str** | path is the path relative to the mount point of the file to project the token into. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


