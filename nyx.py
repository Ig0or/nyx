# Third Party
from decouple import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyfiglet import print_figlet
import uvicorn

# Local
from src.routers.base.base_router import BaseRouter


def build_app() -> FastAPI:
    app = BaseRouter.register_routers()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


if __name__ == "__main__":
    app = build_app()

    print_figlet(text="Nyx", colors="0;0;255")

    port = int(config("SERVER_PORT"))
    uvicorn.run(app=app, host="0.0.0.0", port=port)
