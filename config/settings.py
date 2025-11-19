import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API URLs
    BASE_API_URL = os.getenv('BASE_API_URL')
    BASE_CIAM_URL = os.getenv('BASE_CIAM_URL')
    
    # Authentication
    BASIC_AUTH = os.getenv('BASIC_AUTH')
    API_KEY = os.getenv('API_KEY')
    
    # Security Keys
    AX_FP_KEY = os.getenv('AX_FP_KEY')
    ENCRYPTED_FIELD_KEY = os.getenv('ENCRYPTED_FIELD_KEY')
    XDATA_KEY = os.getenv('XDATA_KEY')
    AX_API_SIG_KEY = os.getenv('AX_API_SIG_KEY')
    X_API_BASE_SECRET = os.getenv('X_API_BASE_SECRET')
    CIRCLE_MSISDN_KEY = os.getenv('CIRCLE_MSISDN_KEY')
    
    # Headers
    UA = os.getenv('UA')
    
    # App Info
    APP_VERSION = "8.9.0"
    DEVICE_TYPE = "Android"
    
    @classmethod
    def validate_config(cls):
        required_vars = [
            'BASE_API_URL', 'BASE_CIAM_URL', 'BASIC_AUTH', 'API_KEY'
        ]
        for var in required_vars:
            if not getattr(cls, var):
                raise ValueError(f"Missing required environment variable: {var}")
