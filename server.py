import os
import asyncio
from fastapi import FastAPI
from app.bot import bot

app = FastAPI()

@app.get("/")
async def health_check():
    print("✅ UptimeRobot ping received!")
    return {"message": "Bot is running!"}

@app.on_event("startup")
async def on_startup():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN is not set")
    asyncio.create_task(bot.start(token))
