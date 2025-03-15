from uuid import uuid4

from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from . import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    text = Column(String)
    done = Column(Boolean, default=False)
