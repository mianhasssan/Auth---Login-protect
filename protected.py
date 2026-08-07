from typing import Optional

from fastapi import APIRouter, Header, HTTPException
from supabase_client import supabase

router = APIRouter(tags=["Protected Routes"])


@router.get("/public/info")
def public_info():
    return {
        "message": "Welcome stranger! This info is public."
    }


@router.get("/protected/profile")
def protected_profile(
    authorization: Optional[str] = Header(None)
):

    # Authorization header missing
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail={"error": "Access token required"}
        )

    # Wrong format
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail={"error": "Access token required"}
        )

    token = authorization.split(" ", 1)[1]

    try:

        # Verify JWT with Supabase
        response = supabase.auth.get_user(token)

        user = response.user

        return {
            "id": user.id,
            "email": user.email,
            "created_at": user.created_at
        }

    except Exception:

        raise HTTPException(
            status_code=401,
            detail={"error": "Invalid or expired token"}
        )