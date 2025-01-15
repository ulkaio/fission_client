# IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution

If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_selector_terms** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsInner.md) | Required. A list of node selector terms. The terms are ORed. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


