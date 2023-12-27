from pydantic import BaseModel


class RecordingMetrics(BaseModel):
    recording_id: str
    create_time: str
    start_time: str
