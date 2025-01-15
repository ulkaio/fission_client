# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerImage

image represents an OCI object (a container image or artifact) pulled and mounted on the kubelet's host machine. The volume is resolved at pod startup depending on which PullPolicy value is provided:  - Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. - Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn't present. - IfNotPresent: the kubelet pulls if the reference isn't already present on disk. Container creation will fail if the reference isn't present and the pull fails.  The volume gets re-resolved if the pod gets deleted and recreated, which means that new remote content will become available on pod recreation. A failure to resolve or pull the image during pod startup will block containers from starting and may add significant latency. Failures will be retried using normal volume backoff and will be reported on the pod reason and message. The types of objects that may be mounted by this volume are defined by the container runtime implementation on a host machine and at minimum must include all valid types supported by the container image field. The OCI object gets mounted in a single directory (spec.containers[*].volumeMounts.mountPath) by merging the manifest layers in the same way as for container images. The volume will be mounted read-only (ro) and non-executable files (noexec). Sub path mounts for containers are not supported (spec.containers[*].volumeMounts.subpath). The field spec.securityContext.fsGroupChangePolicy has no effect on this volume type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_policy** | **str** | Policy for pulling OCI objects. Possible values are: Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn&#39;t present. IfNotPresent: the kubelet pulls if the reference isn&#39;t already present on disk. Container creation will fail if the reference isn&#39;t present and the pull fails. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. | [optional] 
**reference** | **str** | Required: Image or artifact reference to be used. Behaves in the same way as pod.spec.containers[*].image. Pull secrets will be assembled in the same way as for the container image by looking up node credentials, SA image pull secrets, and pod spec image pull secrets. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_image import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerImage

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerImage from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_image_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerImage.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerImage.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_image_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_image_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerImage from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_image_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_image.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


