from sqlalchemy import Column, BigInteger, String, Text, DateTime, Boolean

from database.database import Base


class Notification(Base):
    __tablename__ = "tb_notify_notifications"
    notification_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    content = Column(Text, nullable=False)
    is_read = Column(Boolean, nullable=False)
    reg_dtm = Column(DateTime, nullable=False)
