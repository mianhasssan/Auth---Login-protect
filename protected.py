from fastapi import APIRouter, Depends
from dependencies import get_current_user

router = APIRouter(tags=["Protected Routes"])


@router.get("/public/info")
def public_info():
    return {
        "message": "Welcome stranger! This info is public."
    }


@router.get("/protected/profile")
def protected_profile(user=Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at
    }


@router.get("/protected/dashboard")
def dashboard(user=Depends(get_current_user)):
    return {
        "message": f"Welcome {user.email}",
        "dashboard": "Protected Dashboard"
    }