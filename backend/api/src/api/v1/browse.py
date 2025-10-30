from fastapi import APIRouter, HTTPException

from src import get_logger
from src.core import publish_browse_task
from src.schemas import BrowseRequest, BrowseResponse


logger = get_logger('api.browse')


api_browse_router = APIRouter('/browse', tags=['Browse'])


@api_browse_router.post("/browse", response_model=BrowseResponse)
async def _browse(request: BrowseRequest) -> BrowseResponse:
    try:
        await publish_browse_task(request.url)
        return BrowseResponse(status="queued", message="Task enqueued")
    except Exception as e:
        logger.exception("Failed to enqueue task")
        raise HTTPException(status_code=500, detail=str(e))

__all__ = [
    'api_browse_router'
]
