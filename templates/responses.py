class ResponseTemplates:
    @staticmethod
    def product_display(products: list, title: str = "PRODUK"):
        """Display products template"""
        if not products:
            return f"[!] Tidak ada {title.lower()} ditemukan"
        
        output = f"\n[✓] {title} ({len(products)} items)\n"
        output += "=" * 70 + "\n"
        
        for i, product in enumerate(products, 1):
            output += f"\n{i}. {product.get('name', 'N/A')}\n"
            output += f"   💰 Harga: Rp {product.get('price', 0):,}\n"
            output += f"   📅 Masa Aktif: {product.get('validity', 'N/A')}\n"
            output += f"   📊 Kuota: {product.get('quota', 'N/A')}\n"
            output += f"   🏷️  Kode: {product.get('code', 'N/A')}\n"
            output += f"   🔧 Tipe: {product.get('type', 'Regular')}\n"
            
            if product.get('fam_code'):
                output += f"   👨‍👩‍👧‍👦 FAM Code: {product['fam_code']}\n"
        
        output += "=" * 70
        return output
    
    @staticmethod
    def error_message(message: str):
        """Error message template"""
        return f"[!] Error: {message}"
    
    @staticmethod
    def success_message(message: str):
        """Success message template"""
        return f"[✓] {message}"
    
    @staticmethod
    def info_message(message: str):
        """Info message template"""
        return f"[ℹ] {message}"
