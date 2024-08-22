from bson import ObjectId
from bson.errors import InvalidId

from common import exceptions


async def check_object_id(object_id: str) -> str:
    try:
        object_id = ObjectId(object_id)
    except InvalidId:
        raise exceptions.ObjectIdNotValidException
    else:
        return object_id
