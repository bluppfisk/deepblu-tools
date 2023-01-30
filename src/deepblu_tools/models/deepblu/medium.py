from datetime import datetime

from deepblu_tools.models import uddf as um


# Singular of media, i.c. videos and photos
# This program does not download your videos
# and photos (yet), but it does keep a reference
class Medium:
    def __init__(self, medium: dict):
        self.id = "deepblu_medium_" + medium.get("_id")
        self.url = medium.get("url")
        self.caption = medium.get("caption", "")
        self.datetime = None
        timestamp = medium.get("timestamp")
        if timestamp:
            self.datetime = datetime.fromtimestamp(timestamp).isoformat()
        if medium.get("type") == "Video":
            self.type = "video"
        else:
            self.type = "image"

    def to_uddf(self) -> um.MediaType:
        if self.type == "image":
            return um.ImageType(
                id=self.id,
                objectname=self.url,
                title=self.caption,
                imagedata=um.ImageType.Imagedata(datetime=self.datetime),
            )
        elif self.type == "video":
            return um.MediaType(id=self.id, objectname=self.url, title=self.caption)
