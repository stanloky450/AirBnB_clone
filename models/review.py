from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The review text of the place.
    """

    place_id = ""
    user_id = ""
    text = ""
