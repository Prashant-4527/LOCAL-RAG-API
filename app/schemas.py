from typing import Literal 
from pydantic import BaseModel, Field, field_validator


class HealthResponse(BaseModel):
    status: Literal["ok", "degraded", "down"] = Field(
        ..., description="Current health status of the API"
    )
    message: str = Field(..., min_lenght=1, description="Human-readable status message")



    @field_validator("message")
    @classmethod
    def message_must_not_be_blank(cls, v:str) -> str:
        if not v.strip():
            raise ValueError("Message must not be blank")
        return v.strip()