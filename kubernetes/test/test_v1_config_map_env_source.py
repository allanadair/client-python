# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_config_map_env_source import V1ConfigMapEnvSource


class TestV1ConfigMapEnvSource(unittest.TestCase):
    """ V1ConfigMapEnvSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ConfigMapEnvSource(self):
        """
        Test V1ConfigMapEnvSource
        """
        model = kubernetes.client.models.v1_config_map_env_source.V1ConfigMapEnvSource()


if __name__ == '__main__':
    unittest.main()
