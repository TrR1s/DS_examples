from pydantic import BaseModel, computed_field,field_validator,Field

class SessionFigures(BaseModel):
    hand_amount: int
    result: float
