from typing import Optional

from fastapi import Header, HTTPException
from supabase_client import supabase


def get_current_user(
    authorization: Optional[str] = Header(None)
):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail={"error": "Access token required"}
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail={"error": "Access token required"}
        )

    token = authorization.split(" ", 1)[1]

    try:
        response = supabase.auth.get_user(token)
        return response.user

    except Exception:
        raise HTTPException(
            status_code=401,
            detail={"error": "Invalid or expired token"}
        )