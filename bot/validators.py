import re
from typing import Optional
from decimal import Decimal

class ValidationError(Exception):
    """Custom exception for validation failures."""
    pass

def validate_symbol(symbol: str) -> str:
    """
    Validate symbol e.g., BTCUSDT.
    """
    if not re.match(r'^[A-Z0-9]+USDT$', symbol):
        raise ValidationError(f"Invalid symbol '{symbol}'. Must be uppercase, end with USDT e.g., BTCUSDT")
    return symbol.upper()

def validate_side(side: str) -> str:
    """
    Validate side BUY/SELL.
    """
    side = side.upper()
    if side not in ['BUY', 'SELL']:
        raise ValidationError(f"Invalid side '{side}'. Must be BUY or SELL")
    return side

def validate_order_type(order_type: str) -> str:
    """
    Validate order type MARKET/LIMIT.
    """
    order_type = order_type.upper()
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValidationError(f"Invalid type '{order_type}'. Must be MARKET or LIMIT")
    return order_type

def validate_quantity(qty: str) -> Decimal:
    """
    Validate quantity > 0.
    """
    try:
        qty_dec = Decimal(qty)
        if qty_dec <= 0:
            raise ValidationError(f"Quantity '{qty}' must be > 0")
        return qty_dec
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid quantity '{qty}'. Must be positive number")

def validate_price(price: Optional[str]) -> Optional[Decimal]:
    """
    Validate price > 0 (for LIMIT).
    """
    if price is None:
        return None
    try:
        price_dec = Decimal(price)
        if price_dec <= 0:
            raise ValidationError(f"Price '{price}' must be > 0")
        return price_dec
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid price '{price}'. Must be positive number")

