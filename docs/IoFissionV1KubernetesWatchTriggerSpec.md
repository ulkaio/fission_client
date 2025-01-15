# IoFissionV1KubernetesWatchTriggerSpec

KubernetesWatchTriggerSpec defines spec of KuberenetesWatchTrigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functionref** | [**IoFissionV1KubernetesWatchTriggerSpecFunctionref**](IoFissionV1KubernetesWatchTriggerSpecFunctionref.md) |  | 
**labelselector** | **Dict[str, str]** | Resource labels | [optional] 
**namespace** | **str** |  | 
**type** | **str** | Type of resource to watch (Pod, Service, etc.) | 

## Example

```python
from fission_client.models.io_fission_v1_kubernetes_watch_trigger_spec import IoFissionV1KubernetesWatchTriggerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1KubernetesWatchTriggerSpec from a JSON string
io_fission_v1_kubernetes_watch_trigger_spec_instance = IoFissionV1KubernetesWatchTriggerSpec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1KubernetesWatchTriggerSpec.to_json()

# convert the object into a dict
io_fission_v1_kubernetes_watch_trigger_spec_dict = io_fission_v1_kubernetes_watch_trigger_spec_instance.to_dict()
# create an instance of IoFissionV1KubernetesWatchTriggerSpec from a dict
io_fission_v1_kubernetes_watch_trigger_spec_form_dict = io_fission_v1_kubernetes_watch_trigger_spec.from_dict(io_fission_v1_kubernetes_watch_trigger_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


