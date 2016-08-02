# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from polklibrary.type.computeravailability.testing import POLKLIBRARY_TYPE_COMPUTERAVAILABILITY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that polklibrary.type.computeravailability is properly installed."""

    layer = POLKLIBRARY_TYPE_COMPUTERAVAILABILITY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.type.computeravailability is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('polklibrary.type.computeravailability'))

    def test_browserlayer(self):
        """Test that IPolklibraryTypeComputeravailabilityLayer is registered."""
        from polklibrary.type.computeravailability.interfaces import IPolklibraryTypeComputeravailabilityLayer
        from plone.browserlayer import utils
        self.assertIn(IPolklibraryTypeComputeravailabilityLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_TYPE_COMPUTERAVAILABILITY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['polklibrary.type.computeravailability'])

    def test_product_uninstalled(self):
        """Test if polklibrary.type.computeravailability is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('polklibrary.type.computeravailability'))

    def test_browserlayer_removed(self):
        """Test that IPolklibraryTypeComputeravailabilityLayer is removed."""
        from polklibrary.type.computeravailability.interfaces import IPolklibraryTypeComputeravailabilityLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPolklibraryTypeComputeravailabilityLayer, utils.registered_layers())
