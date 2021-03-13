import fastapi

router = fastapi.APIRouter()


@router.get('/', include_in_schema=False)
async def index():
    return {'NBCV API': 'Go to /docs for more.'}