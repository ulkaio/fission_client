# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGitRepo

gitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory** | **str** | directory is the target directory name. Must not contain or start with &#39;..&#39;.  If &#39;.&#39; is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. | [optional] 
**repository** | **str** | repository is the URL | 
**revision** | **str** | revision is the commit hash for the specified revision. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_git_repo import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGitRepo

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGitRepo from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_git_repo_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGitRepo.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGitRepo.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_git_repo_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_git_repo_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGitRepo from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_git_repo_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_git_repo.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_git_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


