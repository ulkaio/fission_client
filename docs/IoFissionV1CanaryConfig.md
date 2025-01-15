# IoFissionV1CanaryConfig

CanaryConfig is for canary deployment of two functions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) |  | 
**spec** | [**IoFissionV1CanaryConfigSpec**](IoFissionV1CanaryConfigSpec.md) |  | 
**status** | [**IoFissionV1CanaryConfigStatus**](IoFissionV1CanaryConfigStatus.md) |  | 

## Example

```python
from fission_client.models.io_fission_v1_canary_config import IoFissionV1CanaryConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1CanaryConfig from a JSON string
io_fission_v1_canary_config_instance = IoFissionV1CanaryConfig.from_json(json)
# print the JSON string representation of the object
print IoFissionV1CanaryConfig.to_json()

# convert the object into a dict
io_fission_v1_canary_config_dict = io_fission_v1_canary_config_instance.to_dict()
# create an instance of IoFissionV1CanaryConfig from a dict
io_fission_v1_canary_config_form_dict = io_fission_v1_canary_config.from_dict(io_fission_v1_canary_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


