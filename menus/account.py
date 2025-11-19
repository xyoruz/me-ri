from core.auth import AuthManager
from core.utils import Utils

class AccountMenu:
    def __init__(self):
        self.auth = AuthManager()
    
    def login_flow(self) -> bool:
        """Complete login flow with OTP"""
        print("\n" + "="*50)
        print("🔐 LOGIN MYXL ACCOUNT")
        print("="*50)
        
        phone_number = input("[?] Masukkan nomor XL: ").strip()
        
        if not Utils.validate_phone(phone_number):
            print("[!] Nomor tidak valid. Gunakan format: 08xxx atau 62xxx")
            return False
        
        # Send OTP
        otp_result = self.auth.send_otp(phone_number)
        if otp_result['status'] != 'success':
            print(f"[!] Gagal: {otp_result['message']}")
            return False
        
        # Verify OTP
        otp_code = input("[?] Masukkan 6 digit OTP: ").strip()
        if not Utils.validate_otp(otp_code):
            print("[!] OTP harus 6 digit angka")
            return False
        
        verify_result = self.auth.verify_otp(phone_number, otp_code)
        if verify_result['status'] == 'success':
            print("[✓] Login berhasil!")
            return True
        else:
            print(f"[!] Login gagal: {verify_result['message']}")
            return False
    
    def get_account_info(self):
        """Get account information"""
        if not self.auth.is_logged_in:
            print("[!] Silakan login terlebih dahulu")
            return
        
        print("\n[📊 ACCOUNT INFORMATION]")
        print(f"Status: {'Logged In' if self.auth.is_logged_in else 'Logged Out'}")
        if self.auth.token:
            print(f"Token: {self.auth.token[:20]}...")
        print(f"Session: {'Active' if self.auth.is_logged_in else 'Inactive'}")
