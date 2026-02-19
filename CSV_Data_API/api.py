from fastapi import FastAPI, Query, APIRouter
from contextlib import asynccontextmanager
import pandas as pd
from constants import DATA_PATH
from data_processing import DataExplorer

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.df = pd.read_csv(DATA_PATH / "Sales.csv", index_col=0, parse_dates=True)
    yield
    del app.state.df # to clean up afterwards

app = FastAPI(lifespan=lifespan)

router = APIRouter(prefix = "/api/sales")

@router.get("/summary") # @app.get("/api/summary")
async def read_summary_data():
    data = DataExplorer(app.state.df)
    #print(data.describe())
    #return JSONResponse(json.loads(data.describe().to_json()))
    return data.summary().json_response()

@router.get("/kpis") # @app.get("/api/kpis")
async def read_kpis(country: str = Query(None)):
    data = DataExplorer(app.state.df)
    return data.kpis(country)

@router.get("") # @app.get("/api/sales")
async def read_sales(limit: int = Query(100, gt=0, lt=150000)):
    data = DataExplorer(app.state.df, limit)
    return data.json_response()

app.include_router(router)

