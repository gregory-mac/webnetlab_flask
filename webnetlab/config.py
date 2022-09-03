from dotenv import load_dotenv
import os


load_dotenv()


class Config:
    # Containerlab files settings
    path_to_lab_files: str = os.getenv("WEBNETLAB_PATH_TO_LABFILES")
    lab_spec_filename: str = os.getenv("WEBNETLAB_LAB_SPEC_FILENAME")

    # Server settings
    server_ip: str = os.getenv("WEBNETLAB_SERVER_IP")
    server_port: int = os.getenv("WEBNETLAB_SERVER_PORT")
    worker_count: int = os.getenv("WEBNETLAB_SERVER_WORKERS")
    reload_app_on_change: bool = os.getenv("WEBNETLAB_SERVER_RELOAD")
