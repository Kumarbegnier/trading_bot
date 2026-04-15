from .client import BinanceFuturesClient
from .validators import (
    validate_symbol, validate_side, validate_order_type, 
    validate_quantity, validate_price, ValidationError
)
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

def place_market_order(symbol: str, side: str, quantity: str, api_key: str, api_secret: str):
    """
    Place MARKET order with validation.
    """
    try:
        # Validate
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        qty = validate_quantity(quantity)
        
        print("\n=== MARKET Order Request ===")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Quantity: {qty}")
        print("Type: MARKET")
        print("==========================")
        
        # Place order
        client = BinanceFuturesClient(api_key, api_secret)
        order = client.place_market_order(symbol, side, float(qty))
        
        print("\n=== Order Response ===")
        print(f"Order ID: {order.get('orderId', 'N/A')}")
        print(f"Status: {order.get('status', 'N/A')}")
        print(f"Executed Qty: {order.get('executedQty', 'N/A')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")
        print("====================")
        print("✅ MARKET order placed successfully!")
        
        return order
        
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        print(f"❌ Validation error: {e}")
        raise
    except Exception as e:
        logger.error(f"Order placement failed: {e}")
        print(f"❌ Order failed: {e}")
        raise

def place_limit_order(symbol: str, side: str, quantity: str, price: str, api_key: str, api_secret: str):
    """
    Place LIMIT order with validation.
    """
    try:
        # Validate
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        qty = validate_quantity(quantity)
        price_dec = validate_price(price)
        
        print("\n=== LIMIT Order Request ===")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Quantity: {qty}")
        print(f"Price: {price_dec}")
        print("Type: LIMIT (GTC)")
        print("==========================")
        
        # Place order
        client = BinanceFuturesClient(api_key, api_secret)
        order = client.place_limit_order(symbol, side, float(qty), float(price_dec))
        
        print("\n=== Order Response ===")
        print(f"Order ID: {order.get('orderId', 'N/A')}")
        print(f"Status: {order.get('status', 'N/A')}")
        print(f"Executed Qty: {order.get('executedQty', 'N/A')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")
        print("====================")
        print("✅ LIMIT order placed successfully!")
        
        return order
        
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        print(f"❌ Validation error: {e}")
        raise
    except Exception as e:
        logger.error(f"Order placement failed: {e}")
        print(f"❌ Order failed: {e}")
        raise

