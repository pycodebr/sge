from django import template
from decimal import Decimal, InvalidOperation
import locale

register = template.Library()

@register.filter
def currency(value):
    """
    Formats a number as Brazilian currency (R$ XXX.XXX,XX)
    """
    if value is None:
        return "R$ 0,00"
    
    try:
        # Convert to Decimal for precise formatting
        if isinstance(value, str):
            value = Decimal(value.replace(',', '.'))
        elif not isinstance(value, Decimal):
            value = Decimal(str(value))
        
        # Format with Brazilian locale
        formatted_value = f"{value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        return f"R$ {formatted_value}"
        
    except (InvalidOperation, ValueError, TypeError):
        return "R$ 0,00"

@register.filter
def currency_no_symbol(value):
    """
    Formats a number as Brazilian currency without R$ symbol (XXX.XXX,XX)
    """
    if value is None:
        return "0,00"
    
    try:
        # Convert to Decimal for precise formatting
        if isinstance(value, str):
            value = Decimal(value.replace(',', '.'))
        elif not isinstance(value, Decimal):
            value = Decimal(str(value))
        
        # Format with Brazilian locale
        formatted_value = f"{value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        return formatted_value
        
    except (InvalidOperation, ValueError, TypeError):
        return "0,00"