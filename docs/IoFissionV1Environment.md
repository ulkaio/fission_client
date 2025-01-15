# IoFissionV1Environment

Environment is environment for building and running user functions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) |  | 
**spec** | [**IoFissionV1EnvironmentSpec**](IoFissionV1EnvironmentSpec.md) |  | 

## Example

```python
from fission_client.models.io_fission_v1_environment import IoFissionV1Environment

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1Environment from a JSON string
io_fission_v1_environment_instance = IoFissionV1Environment.from_json(json)
# print the JSON string representation of the object
print IoFissionV1Environment.to_json()

# convert the object into a dict
io_fission_v1_environment_dict = io_fission_v1_environment_instance.to_dict()
# create an instance of IoFissionV1Environment from a dict
io_fission_v1_environment_form_dict = io_fission_v1_environment.from_dict(io_fission_v1_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


