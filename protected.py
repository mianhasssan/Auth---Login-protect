from fastapi import APIRouter, Header, HTTPException

router = APIRouter(tags=["Protected Routes"])


@router.get("/public/info")
def public_info():
    return {
        "message": "Welcome stranger! This info is public."
    }


@router.get("/protected/profile")
def protected_profile(authorization: str = Header(default=None)):

    # Check if Authorization header exists
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail={"error": "Access token required"}
        )

    # Check Bearer format
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail={"error": "Access token required"}
        )

    token = authorization.replace("Bearer ", "").strip()

    # Check token is not empty
    if token == "":
        raise HTTPException(
            status_code=401,
            detail={"error": "Access token required"}
        )

    return {
        "message": "Access token received.",
        "token": token
    }