# IoFissionV1KubernetesWatchTriggerSpecFunctionref

The reference to a function for kubewatcher to invoke with when receiving events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functionweights** | **object** | Function Reference by weight. this map contains function name as key and its weight as the value. This is for canary upgrade purpose. | [optional] 
**name** | **str** | Name of the function. | 
**type** | **str** | Type indicates whether this function reference is by name or selector. For now, the only supported reference type is by \&quot;name\&quot;.  Future reference types:   * Function by label or annotation   * Branch or tag of a versioned function   * A \&quot;rolling upgrade\&quot; from one version of a function to another Available value: - name - function-weights | 

## Example

```python
from fission_client.models.io_fission_v1_kubernetes_watch_trigger_spec_functionref import IoFissionV1KubernetesWatchTriggerSpecFunctionref

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1KubernetesWatchTriggerSpecFunctionref from a JSON string
io_fission_v1_kubernetes_watch_trigger_spec_functionref_instance = IoFissionV1KubernetesWatchTriggerSpecFunctionref.from_json(json)
# print the JSON string representation of the object
print IoFissionV1KubernetesWatchTriggerSpecFunctionref.to_json()

# convert the object into a dict
io_fission_v1_kubernetes_watch_trigger_spec_functionref_dict = io_fission_v1_kubernetes_watch_trigger_spec_functionref_instance.to_dict()
# create an instance of IoFissionV1KubernetesWatchTriggerSpecFunctionref from a dict
io_fission_v1_kubernetes_watch_trigger_spec_functionref_form_dict = io_fission_v1_kubernetes_watch_trigger_spec_functionref.from_dict(io_fission_v1_kubernetes_watch_trigger_spec_functionref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


