# IoFissionV1EnvironmentSpec

EnvironmentSpec contains with builder, runtime and some other related environment settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_access_to_external_network** | **bool** | Istio default blocks all egress traffic for safety. To enable accessibility of external network for builder/function pod, set to &#39;true&#39;. (Optional) defaults to &#39;false&#39; | [optional] 
**allowed_functions_per_container** | **str** | (Optional) defaults to &#39;single&#39;. Fission workflow uses &#39;infinite&#39; to load multiple functions in one function pod. Available value: - single - infinite | [optional] 
**builder** | [**IoFissionV1EnvironmentSpecBuilder**](IoFissionV1EnvironmentSpecBuilder.md) |  | [optional] 
**imagepullsecret** | **str** | ImagePullSecret is the secret for Kubernetes to pull an image from a private registry. | [optional] 
**keeparchive** | **bool** | KeepArchive is used by fetcher to determine if the extracted archive or unarchived file should be placed, which is then used by specialize handler. (This is mainly for the JVM environment because .jar is one kind of zip archive.) | [optional] 
**poolsize** | **int** | The initial pool size for environment | [optional] 
**resources** | [**IoFissionV1EnvironmentSpecResources**](IoFissionV1EnvironmentSpecResources.md) |  | [optional] 
**runtime** | [**IoFissionV1EnvironmentSpecRuntime**](IoFissionV1EnvironmentSpecRuntime.md) |  | 
**termination_grace_period** | **int** | The grace time for pod to perform connection draining before termination. The unit is in seconds. (Optional) defaults to 360 seconds | [optional] 
**version** | **int** | Version is the Environment API version  Version \&quot;1\&quot; allows user to run code snippet in a file, and it&#39;s supported by most of the environments except tensorflow-serving.  Version \&quot;2\&quot; supports downloading and compiling user function if source archive is not empty.  Version \&quot;3\&quot; is almost the same with v2, but you&#39;re able to control the size of pre-warm pool of the environment. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec import IoFissionV1EnvironmentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpec from a JSON string
io_fission_v1_environment_spec_instance = IoFissionV1EnvironmentSpec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpec.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_dict = io_fission_v1_environment_spec_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpec from a dict
io_fission_v1_environment_spec_form_dict = io_fission_v1_environment_spec.from_dict(io_fission_v1_environment_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


