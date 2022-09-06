from datetime import date
from typing import Any, Dict, Optional, Tuple
from .djolouser import DjolowinUser

def user_is_valid(user: Optional[DjolowinUser]) -> bool:
    """Return True when user is provided and is not anonymous."""
    return bool(user and not user.is_anonymous)