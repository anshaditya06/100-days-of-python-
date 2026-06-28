import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    WTF_CSRF_ENABLED = True
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024   # 2MB file upload limit
    UPLOAD_FOLDER = 'static/uploads'