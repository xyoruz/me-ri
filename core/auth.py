import requests
import json
from config.settings import Config
from core.utils import Utils

class AuthManager:
    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.is_logged_in = False
        self.setup_headers()
    
    def setup_headers(self):
        """Setup default headers"""
        self.headers = {
            'User-Agent': Config.UA,
            'Content-Type': 'application/json',
            'X-API-Key': Config.API_KEY,
            'ax-fp': Utils.generate_fingerprint(Config.AX_FP_KEY),
            'Authorization': f"Basic {Config.BASIC_AUTH}"
        }
    
    def send_otp(self, phone_number: str) -> dict:
        """Send OTP to phone number"""
        print(f"[+] Mengirim OTP ke {phone_number}...")
        
        endpoint = f"{Config.BASE_CIAM_URL}/api/v2/send-otp"
        formatted_phone = Utils.format_phone_number(phone_number)
        
        payload = {
            "msisdn": formatted_phone,
            "channel": "SMS",
            "language": "id",
            "appVersion": Config.APP_VERSION,
            "deviceId": Utils.generate_device_id(formatted_phone)
        }
        
        signature = Utils.generate_signature(payload, Config.AX_API_SIG_KEY)
        headers = self.headers.copy()
        headers['ax-api-sig'] = signature
        
        try:
            response = self.session.post(endpoint, json=payload, headers=headers, timeout=30)
            return self._handle_response(response, "send_otp")
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def verify_otp(self, phone_number: str, otp_code: str) -> dict:
        """Verify OTP code"""
        print(f"[+] Memverifikasi OTP...")
        
        endpoint = f"{Config.BASE_CIAM_URL}/api/v2/verify-otp"
        formatted_phone = Utils.format_phone_number(phone_number)
        
        payload = {
            "msisdn": formatted_phone,
            "otp": otp_code,
            "appVersion": Config.APP_VERSION,
            "deviceId": Utils.generate_device_id(formatted_phone)
        }
        
        signature = Utils.generate_signature(payload, Config.AX_API_SIG_KEY)
        headers = self.headers.copy()
        headers['ax-api-sig'] = signature
        
        try:
            response = self.session.post(endpoint, json=payload, headers=headers, timeout=30)
            result = self._handle_response(response, "verify_otp")
            
            if result.get('status') == 'success':
                self.token = result.get('access_token')
                if self.token:
                    self.headers['Authorization'] = f"Bearer {self.token}"
                    self.is_logged_in = True
            
            return result
            
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def _handle_response(self, response, action: str) -> dict:
        """Handle API response"""
        try:
            data = response.json()
            
            if response.status_code == 200:
                if data.get('status') == 'SUCCESS':
                    return {
                        "status": "success",
                        "message": data.get('message', 'Success'),
                        "access_token": data.get('accessToken'),
                        "data": data.get('data')
                    }
                else:
                    return {
                        "status": "error", 
                        "message": data.get('message', 'Unknown error')
                    }
            else:
                return {
                    "status": "error",
                    "message": f"HTTP {response.status_code}: {response.text}"
                }
                
        except json.JSONDecodeError:
            return {
                "status": "error",
                "message": f"Invalid JSON response: {response.text}"
      }
