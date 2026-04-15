#!/usr/bin/env python3
"""
Trading Bot CLI for Binance Futures Testnet (Production-Grade Version)
"""

import os
import click
import logging

from bot.orders import place_market_order, place_limit_order

# ---------------- Logging ----------------
logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("cli")


# ---------------- Validation Helpers ----------------
def validate_side(side: str):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("side must be BUY or SELL")
    return side


def validate_quantity(quantity: str):
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError()
        return qty
    except:
        raise ValueError("quantity must be a positive number")


def validate_price(price: str):
    try:
        p = float(price)
        if p <= 0:
            raise ValueError()
        return p
    except:
        raise ValueError("price must be a positive number")


def get_credentials(ctx):
    api_key = ctx.obj.get("API_KEY") or os.getenv("BINANCE_API_KEY")
    api_secret = ctx.obj.get("API_SECRET") or os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise click.UsageError("Missing API credentials (use CLI args or env variables)")

    return api_key, api_secret


# ---------------- CLI Group ----------------
@click.group()
@click.option('--api-key', default=None, help='Binance API Key')
@click.option('--api-secret', default=None, help='Binance API Secret')
@click.pass_context
def cli(ctx, api_key, api_secret):
    """Binance Futures Testnet Trading Bot CLI"""
    ctx.ensure_object(dict)
    ctx.obj['API_KEY'] = api_key
    ctx.obj['API_SECRET'] = api_secret


# ---------------- MARKET ORDER ----------------
@cli.command()
@click.argument('symbol')
@click.argument('side')
@click.argument('quantity')
@click.pass_context
def market(ctx, symbol, side, quantity):
    """Place MARKET order"""

    try:
        api_key, api_secret = get_credentials(ctx)

        symbol = symbol.upper()
        side = validate_side(side)
        quantity = validate_quantity(quantity)

        logger.info(f"MARKET ORDER -> {symbol} {side} {quantity}")

        response = place_market_order(
            symbol, side, quantity, api_key, api_secret
        )

        logger.info(f"RESPONSE: {response}")

        click.echo("\n✅ MARKET ORDER SUCCESS")
        click.echo(f"Order ID     : {response.get('orderId')}")
        click.echo(f"Status       : {response.get('status')}")
        click.echo(f"Executed Qty : {response.get('executedQty')}")
        click.echo(f"Avg Price    : {response.get('avgPrice')}")

    except Exception as e:
        logger.error(f"MARKET ORDER FAILED: {str(e)}")
        click.echo(f"\n❌ Error: {e}", err=True)
        raise click.Abort()


# ---------------- LIMIT ORDER ----------------
@cli.command()
@click.argument('symbol')
@click.argument('side')
@click.argument('quantity')
@click.argument('price')
@click.pass_context
def limit(ctx, symbol, side, quantity, price):
    """Place LIMIT order"""

    try:
        api_key, api_secret = get_credentials(ctx)

        symbol = symbol.upper()
        side = validate_side(side)
        quantity = validate_quantity(quantity)
        price = validate_price(price)

        logger.info(f"LIMIT ORDER -> {symbol} {side} {quantity} @ {price}")

        response = place_limit_order(
            symbol, side, quantity, price, api_key, api_secret
        )

        logger.info(f"RESPONSE: {response}")

        click.echo("\n✅ LIMIT ORDER SUCCESS")
        click.echo(f"Order ID     : {response.get('orderId')}")
        click.echo(f"Status       : {response.get('status')}")
        click.echo(f"Executed Qty : {response.get('executedQty')}")
        click.echo(f"Price        : {response.get('price')}")

    except Exception as e:
        logger.error(f"LIMIT ORDER FAILED: {str(e)}")
        click.echo(f"\n❌ Error: {e}", err=True)
        raise click.Abort()


if __name__ == '__main__':
    cli()