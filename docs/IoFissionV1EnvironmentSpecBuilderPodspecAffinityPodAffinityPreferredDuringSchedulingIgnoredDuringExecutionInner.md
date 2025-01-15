# IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner

The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_affinity_term** | [**IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTerm**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTerm.md) |  | 
**weight** | **int** | weight associated with matching the corresponding podAffinityTerm, in the range 1-100. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


