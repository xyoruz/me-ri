#!/usr/bin/env python3
import sys
import os
from config.settings import Config
from menus.account import AccountMenu
from menus.products import ProductsMenu
from core.utils import Utils

class MYXLApp:
    def __init__(self):
        self.account = AccountMenu()
        self.products = ProductsMenu(self.account.auth)
    
    def banner(self):
        print("""
╔══════════════════════════════════════╗
║           MYXL TOOLS PRO             ║
║     Structured Project Version       ║
║     Cari Produk & FAM Code XL        ║
╚══════════════════════════════════════╝
        """)
    
    def main_menu(self):
        """Main application menu"""
        while True:
            print("\n" + "="*50)
            print("🎯 MYXL TOOLS - MAIN MENU")
            print("="*50)
            print("1. 🔐 Login")
            print("2. 🔍 Cari Produk")
            print("3. 👨‍👩‍👧‍👦 FAM Codes") 
            print("4. 📊 Info Akun")
            print("5. 🚪 Keluar")
            print("="*50)
            
            choice = input("[?] Pilih menu (1-5): ").strip()
            
            if choice == '1':
                self.account.login_flow()
            elif choice == '2':
                self.search_products_menu()
            elif choice == '3':
                self.show_fam_codes()
            elif choice == '4':
                self.account.get_account_info()
            elif choice == '5':
                print("[+] Terima kasih! 👋")
                sys.exit(0)
            else:
                print("[!] Pilihan tidak valid")
    
    def search_products_menu(self):
        """Search products menu"""
        if not self.account.auth.is_logged_in:
            if not self.account.login_flow():
                return
        
        print("\n[🔍 PENCARIAN PRODUK]")
        keyword = input("[?] Masukkan kata kunci: ").strip()
        
        if keyword:
            results = self.products.search_products(keyword)
            self.display_products(results, f"Hasil: '{keyword}'")
        else:
            all_products = self.products.fetch_products()
            self.display_products(all_products, "Semua Produk")
    
    def show_fam_codes(self):
        """Show FAM codes"""
        if not self.account.auth.is_logged_in:
            if not self.account.login_flow():
                return
        
        fam_products = self.products.get_fam_products()
        self.display_products(fam_products, "Produk FAM Code")
    
    def display_products(self, products: list, title: str):
        """Display products in formatted way"""
        if not products:
            print(f"[!] Tidak ada produk ditemukan")
            return
        
        print(f"\n[✓] {title} ({len(products)} items)")
        print("=" * 70)
        
        for i, product in enumerate(products, 1):
            print(f"\n{i}. {product.get('name', 'N/A')}")
            print(f"   💰 Harga: {Utils.format_currency(product.get('price', 0))}")
            print(f"   📅 Masa Aktif: {product.get('validity', 'N/A')}")
            print(f"   📊 Kuota: {product.get('quota', 'N/A')}")
            print(f"   🏷️  Kode: {product.get('code', 'N/A')}")
            print(f"   🔧 Tipe: {product.get('type', 'Regular')}")
            
            if product.get('fam_code'):
                print(f"   👨‍👩‍👧‍👦 FAM Code: {product['fam_code']}")
        
        print("=" * 70)

def main():
    try:
        # Validate configuration
        Config.validate_config()
        
        # Start application
        app = MYXLApp()
        app.banner()
        app.main_menu()
        
    except ValueError as e:
        print(f"[!] Configuration Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Diinterupsi oleh user")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Application Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
