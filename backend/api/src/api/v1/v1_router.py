from fastapi import APIRouter

from .browse import api_browse_router


v1_router = APIRouter(prefix='/v1', tags=['v1'])

v1_router.include_router(api_browse_router)


__all__ = [
    'v1_router'
]
