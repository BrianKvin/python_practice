from datetime import datetime
from random import randint
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic models
class Campaign(BaseModel):
    campaign_id: int
    name: str
    due_date: datetime
    created_at: datetime

class CampaignCreate(BaseModel):
    name: str
    due_date: datetime

# In-memory "database"
data: List[Campaign] = [
    Campaign(
        campaign_id=1,
        name="startup fest",
        due_date=datetime.now(),
        created_at=datetime.now()
    ),
    Campaign(
        campaign_id=2,
        name="summer connect",
        due_date=datetime.now(),
        created_at=datetime.now()
    ),
]

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello world!"}

@app.get("/api/v1/campaigns")
async def read_campaigns() -> dict[str, List[Campaign]]:
    return {"campaigns": data}

@app.get("/api/v1/campaigns/{id}")
async def read_campaign(id: int) -> dict[str, Campaign]:
    for campaign in data:
        if campaign.campaign_id == id:
            return {"campaign": campaign}
    raise HTTPException(status_code=404, detail=f"Campaign {id} not found")

@app.post("/api/v1/campaigns")
async def create_campaign(campaign_create: CampaignCreate) -> dict[str, Campaign]:
    new_campaign = Campaign(
        campaign_id=randint(100, 1000),
        name=campaign_create.name,
        due_date=campaign_create.due_date,
        created_at=datetime.now()
    )
    data.append(new_campaign)
    return {"campaign": new_campaign}

@app.put("/api/v1/campaigns/{id}")
async def update_campaign(id: int, campaign_update: CampaignCreate) -> dict[str, Campaign]:
    for index, campaign in enumerate(data):
        if campaign.campaign_id == id:
            updated_campaign = Campaign(
              campaign_id=id,
              name=campaign_update.name,
              due_date=campaign_update.due_date,
              created_at=campaign.created_at,
            )

            data[index] = updated_campaign
            return {"campaign": updated_campaign}
    raise HTTPException(status_code=404)

@app.delete("/api/v1/campaigns/{id}")
async def update_campaign(id: int) -> Response:
    for index, campaign in enumerate(data):
        if campaign.campaign_id == id:
            data.pop(index)
            return Response(status_code=204)
    raise HTTPException(status_code=404)