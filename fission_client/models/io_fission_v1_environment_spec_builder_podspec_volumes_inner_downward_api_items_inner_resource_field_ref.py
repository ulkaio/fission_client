# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.30.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef(BaseModel):
    """
    Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """ # noqa: E501
    container_name: Optional[StrictStr] = Field(default=None, description="Container name: required for volumes, optional for env vars", alias="containerName")
    divisor: Optional[Dict[str, Any]] = Field(default=None, description="Specifies the output format of the exposed resources, defaults to \"1\"")
    resource: StrictStr = Field(description="Required: resource to select")
    __properties: ClassVar[List[str]] = ["containerName", "divisor", "resource"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "containerName": obj.get("containerName"),
            "divisor": obj.get("divisor"),
            "resource": obj.get("resource")
        })
        return _obj


