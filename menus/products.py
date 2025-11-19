from core.api_client import APIClient
from core.utils import Utils

class ProductsMenu:
    def __init__(self, auth_manager):
        self.auth = auth_manager
        self.api = APIClient(auth_manager)
        self.products = []
    
    def fetch_products(self, category: str = "all") -> list:
        """Fetch products from API"""
        if not self.auth.is_logged_in:
            print("[!] Silakan login terlebih dahulu")
            return []
        
        print(f"[+] Mengambil produk ({category})...")
        
        result = self.api.get_products(category)
        if result['status'] == 'success':
            self.products = self._parse_products(result['data'])
            print(f"[✓] Berhasil mengambil {len(self.products)} produk")
            return self.products
        else:
            print(f"[!] Gagal: {result['message']}")
            self.products = self._get_fallback_products()
            return self.products
    
    def _parse_products(self, data: dict) -> list:
        """Parse products from API response"""
        products = []
        
        if isinstance(data, dict):
            # Try different response formats
            for key in ['data', 'packages', 'products', 'items']:
                if key in data and isinstance(data[key], list):
                    products = data[key]
                    break
            
            # If data is nested
            if not products and 'data' in data and isinstance(data['data'], dict):
                for key in ['packages', 'products', 'services']:
                    if key in data['data'] and isinstance(data['data'][key], list):
                        products = data['data'][key]
                        break
        
        return products or self._get_fallback_products()
    
    def _get_fallback_products(self) -> list:
        """Fallback products if API fails"""
        print("[!] Menggunakan data fallback...")
        return [
            {
                "name": "MYXL 1GB 1Hari",
                "price": 5000,
                "validity": "1 Hari",
                "quota": "1GB",
                "code": "*123*100#",
                "type": "Data"
            },
            {
                "name": "MYXL 3GB 3Hari",
                "price": 10000,
                "validity": "3 Hari",
                "quota": "3GB",
                "code": "*123*101#",
                "type": "Data"
            },
            {
                "name": "MYXL 10GB 7Hari",
                "price": 25000,
                "validity": "7 Hari",
                "quota": "10GB",
                "code": "*123*102#",
                "type": "Data"
            },
            {
                "name": "FAM 5GB 30Hari",
                "price": 30000,
                "validity": "30 Hari", 
                "quota": "5GB",
                "code": "*123*200#",
                "fam_code": "FAM001",
                "type": "FAM"
            },
            {
                "name": "FAM 10GB 30Hari",
                "price": 50000,
                "validity": "30 Hari",
                "quota": "10GB",
                "code": "*123*201#",
                "fam_code": "FAM002",
                "type": "FAM"
            },
            {
                "name": "MYXL Unlimited 1Hari",
                "price": 15000,
                "validity": "1 Hari",
                "quota": "Unlimited",
                "code": "*123*300#",
                "type": "Unlimited"
            }
        ]
    
    def search_products(self, keyword: str) -> list:
        """Search products by keyword"""
        if not self.products:
            self.fetch_products()
        
        keyword = keyword.lower()
        return [
            p for p in self.products 
            if keyword in p.get('name', '').lower() or 
               keyword in p.get('type', '').lower() or
               keyword in p.get('code', '').lower()
        ]
    
    def get_fam_products(self) -> list:
        """Get FAM code products"""
        if not self.products:
            self.fetch_products()
        
        return [
            p for p in self.products 
            if p.get('fam_code') or 'fam' in p.get('type', '').lower()
        ]
    
    def get_new_products(self) -> list:
        """Get new products"""
        if not self.products:
            self.fetch_products()
        
        return [
            p for p in self.products 
            if 'baru' in p.get('type', '').lower() or p.get('is_new', False)
        ]
    
    def get_old_products(self) -> list:
        """Get old products"""
        if not self.products:
            self.fetch_products()
        
        return [
            p for p in self.products 
            if 'lama' in p.get('type', '').lower() or p.get('is_old', False)
          ]
