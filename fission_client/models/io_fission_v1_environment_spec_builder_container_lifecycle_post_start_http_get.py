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
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet(BaseModel):
    """
    HTTPGet specifies the http request to perform.
    """ # noqa: E501
    host: Optional[StrictStr] = Field(default=None, description="Host name to connect to, defaults to the pod IP. You probably want to set \"Host\" in httpHeaders instead.")
    http_headers: Optional[List[IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner]] = Field(default=None, description="Custom headers to set in the request. HTTP allows repeated headers.", alias="httpHeaders")
    path: Optional[StrictStr] = Field(default=None, description="Path to access on the HTTP server.")
    port: Dict[str, Any] = Field(description="Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.")
    scheme: Optional[StrictStr] = Field(default=None, description="Scheme to use for connecting to the host. Defaults to HTTP.")
    __properties: ClassVar[List[str]] = ["host", "httpHeaders", "path", "port", "scheme"]

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
        """Create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in http_headers (list)
        _items = []
        if self.http_headers:
            for _item in self.http_headers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['httpHeaders'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host": obj.get("host"),
            "httpHeaders": [IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner.from_dict(_item) for _item in obj.get("httpHeaders")] if obj.get("httpHeaders") is not None else None,
            "path": obj.get("path"),
            "port": obj.get("port"),
            "scheme": obj.get("scheme")
        })
        return _obj


