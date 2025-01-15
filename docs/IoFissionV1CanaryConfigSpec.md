# IoFissionV1CanaryConfigSpec

CanaryConfigSpec defines the canary configuration spec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | Weight increment interval, string representation of time.Duration, ex : 1m, 2h, 2d (default: \&quot;2m\&quot;) | [optional] 
**failure_type** | **str** | FailureType refers to the type of failure | [optional] 
**failurethreshold** | **int** | Threshold in percentage beyond which the new version of the function is considered unstable | [optional] 
**newfunction** | **str** | New version of the function | 
**oldfunction** | **str** | Old stable version of the function | 
**trigger** | **str** | HTTP trigger that this config references | 
**weightincrement** | **int** | Weight increment step for function | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_canary_config_spec import IoFissionV1CanaryConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1CanaryConfigSpec from a JSON string
io_fission_v1_canary_config_spec_instance = IoFissionV1CanaryConfigSpec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1CanaryConfigSpec.to_json()

# convert the object into a dict
io_fission_v1_canary_config_spec_dict = io_fission_v1_canary_config_spec_instance.to_dict()
# create an instance of IoFissionV1CanaryConfigSpec from a dict
io_fission_v1_canary_config_spec_form_dict = io_fission_v1_canary_config_spec.from_dict(io_fission_v1_canary_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


