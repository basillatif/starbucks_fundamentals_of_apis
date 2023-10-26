import connexion
import six

from swagger_server.models.coffee import Coffee  # noqa: E501
from swagger_server.models.coffee1 import Coffee1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def coffee_create(coffee):  # noqa: E501
    """Create a coffee drink and add it to the coffee list

    Create a new drink in the coffee list # noqa: E501

    :param coffee: Coffee to create
    :type coffee: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        coffee = Coffee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def coffee_delete(coffee_name):  # noqa: E501
    """Delete a coffee drink

    Delete a coffee drink in the coffee object # noqa: E501

    :param coffee_name: Name the drink to Delete
    :type coffee_name: str

    :rtype: None
    """
    return 'do some magic!'


def coffee_read():  # noqa: E501
    """The coffee data structure for our server application

    Read the list of coffee drinks # noqa: E501


    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'


def coffee_read_one(coffee_name):  # noqa: E501
    """Read one drink from the coffee object

    Read one drink from the coffee object # noqa: E501

    :param coffee_name: Name of coffee get from the list
    :type coffee_name: str

    :rtype: object
    """
    return 'do some magic!'


def coffee_update(coffee_name, coffee=None):  # noqa: E501
    """Update a coffee drink

    Update a coffee drink in the coffee object # noqa: E501

    :param coffee_name: Name the drink to update
    :type coffee_name: str
    :param coffee: 
    :type coffee: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        coffee = Coffee1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
