from fastapi import FastAPI

from poll.routers import router as poll_urls

app = FastAPI(title="poll service")
app.include_router(poll_urls)
