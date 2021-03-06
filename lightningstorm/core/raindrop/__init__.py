from typing import Dict
from uuid import UUID
from datetime import datetime, timezone
from email.mime.base import MIMEBase
from email.message import EmailMessage
import email.policy
import email.contentmanager


class AbstractRaindrop:
    pass


class LocalFilesystemRainddrop(AbstractRaindrop):
    pass


class MemoryRaindrop(AbstractRaindrop):
    def __init__(
        self,
        uuid: UUID,
        payload: bytes,
        content_type="application/octet-stream",
        content_length: int = None,
        extra_headers: Dict[str, str] = None,
        created_date: datetime = None,
    ):
        self.uuid = uuid
        self.payload = payload
        self.content_type = content_type
        self.extra_headers = extra_headers
        self.created_date = created_date
        self.content_length = content_length
        # default attrs
        self._default_attrs()

    def _default_attrs(self):
        if self.extra_headers is None:
            self.extra_headers = {}
        if self.created_date is None:
            self.created_date = datetime.now(timezone.utc)
        if self.content_length is None:
            self.content_length = len(self.payload)

    def get_headers(self) -> Dict[str, str]:
        extra_headers = self.extra_headers.copy()  # type: ignore
        extra_headers.update(
            {
                "UUID": str(self.uuid),
                "Created-Date": self.created_date.isoformat(),  # type: ignore
                "Content-Type": self.content_type,
                "Content-Lenght": str(self.content_length),
            }
        )
        return extra_headers

    def to_mime(self):
        headers = {"MIME-Version": "1.0"}
        headers.update(self.get_headers())
        maintype, subtype = self.content_type.split("/")
        # mime = MIMEBase(maintype, subtype, **headers)
        # return mime.as_string()
        message = EmailMessage(policy=email.policy.HTTP)
        # message.set_type(self.content_type)
        # message.set_content(
        #     self.payload, maintype=maintype, subtype=subtype, cte="binary",
        # )
        for header, value in headers.items():
            message.add_header(header, value)
        # message.attach(self.payload)
        message.set_payload(self.payload)
        return message.as_bytes()
