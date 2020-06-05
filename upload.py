from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os


def main(file_path, credentials_dict, my_bucket, Cam):
    # Get Google Cloud information.
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict
    )
    client = storage.Client(credentials=credentials, project='myproject')
    bucket = client.get_bucket(my_bucket)

    # Upload all files in local storage.
    file_path = file_path + "{}"
    for i in range(Cam.uploads):
        vid = file_path.format(str(i)) + ".h264"
        blob = bucket.blob(vid)
        blob.upload_from_filename(vid)
        print("File uploaded to Google Cloud!")
        os.remove(vid)
        print("File removed from local storage.")
    Cam.uploads = 0
