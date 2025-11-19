import hashlib
import time
import json
import random
import string

class Utils:
    @staticmethod
    def generate_device_id(msisdn: str) -> str:
        """Generate device ID based on msisdn"""
        return f"termux_{hashlib.md5(msisdn.encode()).hexdigest()[:16]}"
    
    @staticmethod
    def generate_fingerprint(ax_fp_key: str) -> str:
        """Generate device fingerprint"""
        timestamp = str(int(time.time() * 1000))
        data = f"{timestamp}{ax_fp_key}"
        return hashlib.md5(data.encode()).hexdigest()
    
    @staticmethod
    def generate_signature(data: dict, sig_key: str) -> str:
        """Generate API signature"""
        if isinstance(data, dict):
            data = json.dumps(data, separators=(',', ':'))
        signature_data = data + sig_key
        return hashlib.md5(signature_data.encode()).hexdigest()
    
    @staticmethod
    def format_phone_number(phone: str) -> str:
        """Format phone number to international format"""
        phone = ''.join(filter(str.isdigit, phone))
        if phone.startswith('0'):
            return '62' + phone[1:]
        elif phone.startswith('8'):
            return '62' + phone
        return phone
    
    @staticmethod
    def format_currency(amount: int) -> str:
        """Format currency to Indonesian format"""
        return f"Rp {amount:,}"
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate phone number"""
        if not phone or len(phone) < 10:
            return False
        return phone.startswith(('08', '62', '+62'))
    
    @staticmethod
    def validate_otp(otp: str) -> bool:
        """Validate OTP code"""
        return len(otp) == 6 and otp.isdigit()
