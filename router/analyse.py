"""
记忆分析页面
"""

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from orm.schemas.analyse import ParamsAnalyseModel, ReadAnalyseModel, SummaryAnalyseModel
from orm.schemas.generic import GenericResponse
from orm.models import User
from dependencies.orm import get_session
from dependencies.auth import jwt_get_current_user
from orm.crud import query_recode_by_date_user
import settings

router = APIRouter(prefix="/analyse", tags=["分析相关"])


@router.get("/")
async def index():
    return {"index": "analyse"}


@router.post("/review", response_model=GenericResponse[List[ReadAnalyseModel]])
async def analyse_review(data: ParamsAnalyseModel, session: Session = Depends(get_session),
                         user: User = Depends(jwt_get_current_user)):
    data = query_recode_by_date_user(session=session, uid=user.id,
                                     oid=settings.OPERATION_DATA["review_card"],
                                     min_date=data.start_date, max_date=data.end_date)

    return {
        "status": 1,
        "msg": "获取成功",
        "data": data
    }


@router.post("/create", response_model=GenericResponse[List[ReadAnalyseModel]])
async def analyse_create(data: ParamsAnalyseModel, session: Session = Depends(get_session),
                         user: User = Depends(jwt_get_current_user)):
    data = query_recode_by_date_user(session=session, uid=user.id,
                                     oid=settings.OPERATION_DATA["create_card"],
                                     min_date=data.start_date, max_date=data.end_date)

    return {
        "status": 1,
        "msg": "获取成功",
        "data": data
    }
