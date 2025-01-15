# IoFissionV1PackageSpecDeployment

Deployment is the deployable archive that environment runtime used to run user function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | [**IoFissionV1PackageSpecDeploymentChecksum**](IoFissionV1PackageSpecDeploymentChecksum.md) |  | [optional] 
**literal** | **bytearray** | Literal contents of the package. Can be used for encoding packages below TODO (256 KB?) size. | [optional] 
**type** | **str** | Type defines how the package is specified: literal or URL. Available value:  - literal  - url | [optional] 
**url** | **str** | URL references a package. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_package_spec_deployment import IoFissionV1PackageSpecDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1PackageSpecDeployment from a JSON string
io_fission_v1_package_spec_deployment_instance = IoFissionV1PackageSpecDeployment.from_json(json)
# print the JSON string representation of the object
print IoFissionV1PackageSpecDeployment.to_json()

# convert the object into a dict
io_fission_v1_package_spec_deployment_dict = io_fission_v1_package_spec_deployment_instance.to_dict()
# create an instance of IoFissionV1PackageSpecDeployment from a dict
io_fission_v1_package_spec_deployment_form_dict = io_fission_v1_package_spec_deployment.from_dict(io_fission_v1_package_spec_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


