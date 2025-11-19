from menus.products import ProductsMenu

class FamCodesMenu:
    def __init__(self, auth_manager):
        self.products_menu = ProductsMenu(auth_manager)
    
    def show_all_fam_codes(self):
        """Show all FAM codes"""
        fam_products = self.products_menu.get_fam_products()
        
        if not fam_products:
            print("[!] Tidak ada produk FAM code ditemukan")
            return
        
        print(f"\n[👨‍👩‍👧‍👦 SEMUA FAM CODES] ({len(fam_products)} items)")
        print("=" * 70)
        
        for i, product in enumerate(fam_products, 1):
            print(f"\n{i}. {product.get('name', 'N/A')}")
            print(f"   💰 Harga: {product.get('price', 'N/A')}")
            print(f"   📅 Masa Aktif: {product.get('validity', 'N/A')}")
            print(f"   📊 Kuota: {product.get('quota', 'N/A')}")
            print(f"   🏷️  Kode: {product.get('code', 'N/A')}")
            print(f"   🔑 FAM Code: {product.get('fam_code', 'N/A')}")
            print(f"   🔧 Tipe: {product.get('type', 'Regular')}")
        
        print("=" * 70)
    
    def search_fam_code(self, code: str):
        """Search specific FAM code"""
        fam_products = self.products_menu.get_fam_products()
        
        if not fam_products:
            print("[!] Tidak ada produk FAM code ditemukan")
            return
        
        results = [
            p for p in fam_products 
            if code.lower() in p.get('fam_code', '').lower()
        ]
        
        if not results:
            print(f"[!] FAM code '{code}' tidak ditemukan")
            return
        
        print(f"\n[🔍 HASIL PENCARIAN FAM CODE: '{code}']")
        print("=" * 70)
        
        for i, product in enumerate(results, 1):
            print(f"\n{i}. {product.get('name', 'N/A')}")
            print(f"   💰 Harga: {product.get('price', 'N/A')}")
            print(f"   📅 Masa Aktif: {product.get('validity', 'N/A')}")
            print(f"   📊 Kuota: {product.get('quota', 'N/A')}")
            print(f"   🏷️  Kode: {product.get('code', 'N/A')}")
            print(f"   🔑 FAM Code: {product.get('fam_code', 'N/A')}")
        
        print("=" * 70)
