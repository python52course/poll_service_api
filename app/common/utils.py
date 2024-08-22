from bson import ObjectId
from bson.errors import InvalidId

from common import exceptions


async def check_object_id(object_id: str) -> str:
    """
    Checks if the object ID is valid.

    Args:
        object_id (str): The object ID.
    Returns:
        str: The validated object ID.
    Raises:
        exceptions.ObjectIdNotValidException: If the object ID is not valid.
    """
    try:
        object_id = ObjectId(object_id)
    except InvalidId:
        raise exceptions.ObjectIdNotValidException
    else:
        return object_id
