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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner

class TestIoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner(
                pod_affinity_term = fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term.io_fission_v1_Environment_spec_builder_podspec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_podAffinityTerm(
                    label_selector = fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector.io_fission_v1_Environment_spec_builder_podspec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_podAffinityTerm_labelSelector(
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
                    match_label_keys = [
                        ''
                        ], 
                    mismatch_label_keys = [
                        ''
                        ], 
                    namespace_selector = fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector.io_fission_v1_Environment_spec_builder_podspec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_podAffinityTerm_namespaceSelector(), 
                    namespaces = [
                        ''
                        ], 
                    topology_key = '', ),
                weight = 56
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner(
                pod_affinity_term = fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term.io_fission_v1_Environment_spec_builder_podspec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_podAffinityTerm(
                    label_selector = fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector.io_fission_v1_Environment_spec_builder_podspec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_podAffinityTerm_labelSelector(
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
                    match_label_keys = [
                        ''
                        ], 
                    mismatch_label_keys = [
                        ''
                        ], 
                    namespace_selector = fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector.io_fission_v1_Environment_spec_builder_podspec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_podAffinityTerm_namespaceSelector(), 
                    namespaces = [
                        ''
                        ], 
                    topology_key = '', ),
                weight = 56,
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
