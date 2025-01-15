# IoFissionV1TimeTriggerSpec

TimeTriggerSpec invokes the specific function at a time or times specified by a cron string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | **str** | Cron schedule | 
**functionref** | [**IoFissionV1TimeTriggerSpecFunctionref**](IoFissionV1TimeTriggerSpecFunctionref.md) |  | 
**method** | **str** | HTTP Method for trigger, ex : GET, POST, PUT, DELETE, HEAD (default: \&quot;POST\&quot;) | [optional] 
**subpath** | **str** | Subpath to trigger a specific route if function internally supports routing, (default: \&quot;/\&quot;) | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_time_trigger_spec import IoFissionV1TimeTriggerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1TimeTriggerSpec from a JSON string
io_fission_v1_time_trigger_spec_instance = IoFissionV1TimeTriggerSpec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1TimeTriggerSpec.to_json()

# convert the object into a dict
io_fission_v1_time_trigger_spec_dict = io_fission_v1_time_trigger_spec_instance.to_dict()
# create an instance of IoFissionV1TimeTriggerSpec from a dict
io_fission_v1_time_trigger_spec_form_dict = io_fission_v1_time_trigger_spec.from_dict(io_fission_v1_time_trigger_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


