from sqlalchemy import String, Boolean, Column, Integer, Text, TIMESTAMP
from enum import Enum
from .enums import DeviceType

from .dao import Base


class Installation(Base):
    __tablename__ = "installations"

    id = Column(Integer, primary_key=True, nullable=False)
    device_name = Column(String, nullable=False)
    # device_type = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Boolean, default=True)
    # created_at = Column(TIMESTAMP, nullable=False, server_default=Text('now()'))
    updated_at = Column(TIMESTAMP, nullable=False)

