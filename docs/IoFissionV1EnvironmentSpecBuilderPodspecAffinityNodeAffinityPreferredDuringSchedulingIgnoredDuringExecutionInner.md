# IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner

An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preference** | [**IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference.md) |  | 
**weight** | **int** | Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


