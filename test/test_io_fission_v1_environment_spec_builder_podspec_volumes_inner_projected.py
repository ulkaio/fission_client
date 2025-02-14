# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.30.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected(
                default_mode = 56,
                sources = [
                    fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_projected_sources_inner(
                        cluster_trust_bundle = fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_projected_sources_inner_clusterTrustBundle(
                            label_selector = fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_label_selector.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_projected_sources_inner_clusterTrustBundle_labelSelector(
                                match_expressions = [
                                    fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner.io_fission_v1_Environment_spec_builder_podspec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_podAffinityTerm_labelSelector_matchExpressions_inner(
                                        key = '', 
                                        operator = '', 
                                        values = [
                                            ''
                                            ], )
                                    ], 
                                match_labels = {
                                    'key' : ''
                                    }, ), 
                            name = '', 
                            optional = True, 
                            path = '', 
                            signer_name = '', ), 
                        config_map = fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_config_map.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_projected_sources_inner_configMap(
                            items = [
                                fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map_items_inner.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_configMap_items_inner(
                                    key = '', 
                                    mode = 56, 
                                    path = '', )
                                ], 
                            name = '', 
                            optional = True, ), 
                        downward_api = fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_downward_api.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_projected_sources_inner_downwardAPI(), 
                        secret = fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_secret.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_projected_sources_inner_secret(
                            name = '', 
                            optional = True, ), 
                        service_account_token = fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_projected_sources_inner_serviceAccountToken(
                            audience = '', 
                            expiration_seconds = 56, 
                            path = '', ), )
                    ]
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
