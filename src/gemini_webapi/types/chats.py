from pydantic import BaseModel

class Chat(BaseModel):
    """
    A single reply candidate object in the model output. A full response from Gemini usually contains multiple reply candidates.

    Parameters
    ----------
    cid: `str`
        Reply candidate ID to build the metadata
    name: `str`
        Chat Name
    """

    cid: str
    name: str

class Chats(BaseModel):
    """
    A single reply candidate object in the model output. A full response from Gemini usually contains multiple reply candidates.

    Parameters
    ----------
    Chats: `list[Chat]`
    """

    chats: list[Chat]
