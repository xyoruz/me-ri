import requests
from config.settings import Config
from core.utils import Utils

class APIClient:
    def __init__(self, auth_manager):
        self.auth = auth_manager
        self.session = requests.Session()
    
    def get_products(self, category: str = "all") -> dict:
        """Get products from API"""
        if not self.auth.is_logged_in:
            return {"status": "error", "message": "Not logged in"}
        
        endpoints = {
            "all": "/api/v1/products",
            "data": "/api/v1/products/data",
            "fam": "/api/v1/products/fam", 
            "package": "/api/v1/products/packages"
        }
        
        endpoint = endpoints.get(category, endpoints["all"])
        url = Config.BASE_API_URL + endpoint
        
        signature = Utils.generate_signature({"category": category}, Config.AX_API_SIG_KEY)
        headers = self.auth.headers.copy()
        headers['ax-api-sig'] = signature
        
        try:
            response = self.session.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                return {
                    "status": "success",
                    "data": response.json()
                }
            else:
                return {
                    "status": "error",
                    "message": f"HTTP {response.status_code}"
                }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def get_account_info(self) -> dict:
        """Get account information"""
        if not self.auth.is_logged_in:
            return {"status": "error", "message": "Not logged in"}
        
        endpoint = "/api/v1/account/profile"
        url = Config.BASE_API_URL + endpoint
        
        signature = Utils.generate_signature({"action": "profile"}, Config.AX_API_SIG_KEY)
        headers = self.auth.headers.copy()
        headers['ax-api-sig'] = signature
        
        try:
            response = self.session.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                return {
                    "status": "success",
                    "data": response.json()
                }
            else:
                return {
                    "status": "error",
                    "message": f"HTTP {response.status_code}"
                }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
