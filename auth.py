from fastapi import APIRouter, HTTPException
from models import UserAuth
from supabase_client import supabase
from fastapi import Depends
from fastapi.responses import Response
from dependencies import get_current_user
from supabase_client import supabase

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", status_code=201)
def signup(user: UserAuth):

    if not user.email or not user.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required."
        )

    response = supabase.auth.sign_up(
        {
            "email": user.email,
            "password": user.password
        }
    )

    return response


@router.post("/login")
def login(user: UserAuth):

    if not user.email or not user.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required."
        )

    try:

        response = supabase.auth.sign_in_with_password(
            {
                "email": user.email,
                "password": user.password
            }
        )

        return {
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token,
            "user": response.user
        }

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid login credentials"
        )
    


@router.post("/logout", status_code=204)
def logout(
    user = Depends(get_current_user)
):
    supabase.auth.sign_out()
    return Response(status_code=204)