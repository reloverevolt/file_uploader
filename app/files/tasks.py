from celery import shared_task
from files.handlers import File, FileHandler, handler_map


@shared_task
def process_file_task(file_id):
    file = File.objects.get(id=file_id)
    handler_class = handler_map.get(file.get_file_extension(), FileHandler)
    handler_class(file).process()
