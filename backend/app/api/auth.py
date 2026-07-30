from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth_schema import UserRegister, UserLogin
from app.core.security import ( hash_password, verify_password, create_access_token)
from app.db.models import User
from app.db.session import get_db
from app.core.oauth2 import get_current_user
from app.db.models import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
    ):


    existing_user = db.query(User).filter(
    User.email == user.email
    ).first()

    if existing_user:
      raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Email already registered"
      )

    hashed_password = hash_password(user.password)

    new_user = User(
    name=user.name,
    email=user.email,
    password=hashed_password
)
    
    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
    "message": "User registered successfully",
    "id": new_user.id,
    "name": new_user.name,
    "email": new_user.email
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
    User.email == form_data.username
    
    ).first()

    if not existing_user:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password"
    )

    if not verify_password(form_data.password, existing_user.password):
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password"
    )

    access_token = create_access_token(
    data={"sub": existing_user.email})

    return {
    "access_token": access_token,
    "token_type": "bearer"
    }

@router.get("/profile")
def get_profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "created_at": current_user.created_at
    }