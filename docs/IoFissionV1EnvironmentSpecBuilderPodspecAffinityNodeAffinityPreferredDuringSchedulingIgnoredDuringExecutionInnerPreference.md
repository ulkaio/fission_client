# IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference

A node selector term, associated with the corresponding weight.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner.md) | A list of node selector requirements by node&#39;s labels. | [optional] 
**match_fields** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner.md) | A list of node selector requirements by node&#39;s fields. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


