from fastapi import FastAPI

from poll.handlers import router as poll_urls

app = FastAPI(title="Сервис голосования")
app.include_router(poll_urls)
