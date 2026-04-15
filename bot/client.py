from binance.client import Client
from binance.exceptions import BinanceAPIException
from .logging_config import setup_logging
import logging

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    """
    Wrapper for Binance Futures Testnet client.
    """
    
    def __init__(self, api_key: str, api_secret: str):
        setup_logging()
        self.client = Client(api_key, api_secret, testnet=True)
        logger.info("Binance Futures Testnet client initialized")
    
    def place_market_order(self, symbol: str, side: str, quantity: float) -> dict:
        """
        Place MARKET order.
        """
        try:
            logger.info(f"Placing MARKET {side} order: {symbol}, qty={quantity}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logger.info(f"MARKET order successful: orderId={order['orderId']}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
    
    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float) -> dict:
        """
        Place LIMIT order.
        """
        try:
            logger.info(f"Placing LIMIT {side} order: {symbol}, qty={quantity}, price={price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            logger.info(f"LIMIT order successful: orderId={order['orderId']}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise

