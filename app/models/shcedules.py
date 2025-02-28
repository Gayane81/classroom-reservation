from mongoengine import Document, EmbeddedDocument, StringField, IntField, DateTimeField, EnumField, BooleanField, EmbeddedDocumentField
from enum import Enum

class ActivityType(Enum):
  MEETING = "meeting"
  LECTURE = "lecture"
  WORKSHOP = "workshop"
  PROJECT = "project"
  OTHER = "other"

class Room(EmbeddedDocument):
  name = StringField(required=True)
  capacity = IntField(required=True, max_value=30)

class Schedule(Document):
  rooms = EmbeddedDocumentField(Room)
  start = DateTimeField(required=True)
  end = DateTimeField(required=True)
  group_name = StringField(required=True)
  activity = EnumField(ActivityType, required=True)
  is_fixed = BooleanField(required=True)

  def to_dict(self):
        return {
            "rooms": {
                "name": self.rooms.name,
                "capacity": self.rooms.capacity
            },
            "start": self.start,
            "end": self.end,
            "group_name": self.group_name,
            "activity": self.activity.value,
            "is_fixed": self.is_fixed
        }