from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status


def convert_to_bson_object_id(object_id: str) -> str:
    """
    Convert a string to a bson ObjectId.

    Args:
        object_id (str): The string to convert.

    Returns:
        str: The bson ObjectId.

    Raises:
        HTTPException: If the object_id is not valid.
    """
    try:
        object_id = ObjectId(object_id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="poll_id is not valid, poll_id must be 24 character",
        )
    else:
        return object_id
