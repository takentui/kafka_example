from typing import AsyncGenerator

import pytest
from sqlalchemy.sql import text

from app import db
from app.db.registry import registry as db_registry

TRUNCATE_QUERY = "TRUNCATE TABLE {tbl_name} CASCADE;"


@pytest.fixture
async def clear_db() -> AsyncGenerator[None, None]:
    yield
    async with db_registry.engine.begin() as conn:
        await conn.execute(text(TRUNCATE_QUERY.format(tbl_name=db.customer_info.Customer.__tablename__)))
