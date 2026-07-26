# carrito.py

from typing import Dict, Any, Optional

class Carrito:
    # REQUISITO: Tipar explícitamente el diccionario de productos
    # Cada producto es un diccionario con claves str (precio, cantidad) y valores mezclados (float/int)
    productos: Dict[str, Dict[str, Any]]

    def __init__(self) -> None:
        self.productos = {}

    def agregar_producto(self, nombre: str, precio: float, cantidad: int = 1) -> None:
        if precio <= 0 or cantidad <= 0:
            raise ValueError("Precio y cantidad deben ser mayores a cero")
        
        if nombre in self.productos:
            self.productos[nombre]["cantidad"] += cantidad
        else:
            self.productos[nombre] = {"precio": precio, "cantidad": cantidad}

    def calcular_subtotal(self) -> float:
        subtotal: float = 0.0
        for item in self.productos.values():
            subtotal += item["precio"] * item["cantidad"]
        return subtotal
#________________________CAMBIAR STR POR INT!!!!!!!_____________________________
    def aplicar_descuento(self, codigo: str) -> float:
        subtotal = self.calcular_subtotal()
        if codigo == "BIENVENIDA":
            return subtotal * 0.90  # 10% de descuento corregido
        elif codigo == "PROMO50":
            return subtotal * 0.5
        return subtotal

    def calcular_total_con_envio(self, codigo_descuento: Optional[str] = None) -> float:
        # Nota el uso de Optional[str] para cuando no se envía código
        total = self.aplicar_descuento(codigo_descuento if codigo_descuento else "")
        if total < 100:
            total += 15
        return total
# ruff check carrito.py  
# mypy --strict carrito.py
