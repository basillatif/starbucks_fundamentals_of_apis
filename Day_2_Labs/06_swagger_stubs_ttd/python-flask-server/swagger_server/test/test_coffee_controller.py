# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.coffee import Coffee  # noqa: E501
from swagger_server.models.coffee1 import Coffee1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCoffeeController(BaseTestCase):
    """CoffeeController integration test stubs"""

    def test_coffee_create(self):
        """Test case for coffee_create

        Create a coffee drink and add it to the coffee list
        """
        coffee = Coffee()
        response = self.client.open(
            '/api/coffee',
            method='POST',
            data=json.dumps(coffee),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_coffee_delete(self):
        """Test case for coffee_delete

        Delete a coffee drink
        """
        response = self.client.open(
            '/api/coffee/{coffee_name}'.format(coffee_name='coffee_name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_coffee_read(self):
        """Test case for coffee_read

        The coffee data structure for our server application
        """
        response = self.client.open(
            '/api/coffee',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_coffee_read_one(self):
        """Test case for coffee_read_one

        Read one drink from the coffee object
        """
        response = self.client.open(
            '/api/coffee/{coffee_name}'.format(coffee_name='coffee_name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_coffee_update(self):
        """Test case for coffee_update

        Update a coffee drink
        """
        coffee = Coffee1()
        response = self.client.open(
            '/api/coffee/{coffee_name}'.format(coffee_name='coffee_name_example'),
            method='PUT',
            data=json.dumps(coffee),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
