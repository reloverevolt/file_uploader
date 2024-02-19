import logging
import random

from files.models import File


logging.basicConfig(level=logging.INFO)


class BlackBoxException(Exception):
    ...


def black_box_process(file: File):
    result = random.choice([True, True, False])
    if not result:
        raise BlackBoxException("Error occurred while processing the file")


class FileHandler:
    def __init__(self, file: File):
        self.file = file

    def update_status(self, status: str):
        self.file.status = status
        self.file.save()

    def process(self) -> File:
        try:
            black_box_process(self.file)
            self.update_status(File.Status.PROCESSED)
        except BlackBoxException as err:
            self.file.errors = dict(reason=str(err))
            self.update_status(File.Status.FAILED)


class AudioFileHandler(FileHandler):
    def process(self) -> File:
        logging.info("Processing Audio File")
        super().process()


class ImageFileHandler(FileHandler):
    def process(self) -> File:
        logging.info("Processing Image File")
        super().process()


class TextFileHandler(FileHandler):
    def process(self) -> File:
        logging.info("Processing Text File")
        super().process()


handler_map = {
    "png": ImageFileHandler,
    "jpg": ImageFileHandler,
    "mp3": AudioFileHandler,
    "txt": TextFileHandler
}
