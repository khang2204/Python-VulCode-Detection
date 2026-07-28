class Meta:
    db_table = "app_benefits"

# uploaded_file expects to be a UploadedFile object from request.FILES
# in Django
# this way of saving data leaves intended vulnerability
@staticmethod
def save_data(uploaded_file, backup=None):
    data_path = os.path.join(settings.MEDIA_ROOT, "data")
    full_file_name = os.path.join(data_path, uploaded_file.name)
    # the uploaded file is read at once, as duplicated in railsgoat
    # use file.chunk() in a loop can prevent overwhelming system memory
    content = ContentFile(uploaded_file.read())
    default_storage.save(full_file_name, content)
    # using string "true" is intended to duplicate railsgoat's behavior
    if backup == "true":
        return Benefits.make_backup(uploaded_file, data_path,
                                    full_file_name)

def silence_streams(func):
    def wrapper(*args, **kwargs):
        # save stderr
        save_streams = sys.__stderr__
        save_streams.flush()
