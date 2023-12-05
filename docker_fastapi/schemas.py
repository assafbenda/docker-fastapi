from pydantic import BaseModel
import datetime as dt
from .enums import DeviceType


class Installations(BaseModel):
    device_name: str = 'Dummy Device'
    # device_type: DeviceType = DeviceType.OTHER
    description: str = None
    status: bool = True
    updated_at: dt.datetime = dt.datetime.now().isoformat()
