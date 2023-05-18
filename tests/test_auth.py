from sqlalchemy import select, insert

from conftest import client, async_session_maker
from authdir.models import role


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, role_name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'admin', None)], "Роль не добавилась"


def test_register():
    response = client.post(
        '/auth/register',
        json={
            "email": "fastapi_tst@mail.ru",
            "password": "string",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "string",
            "role_id": 1
        }
    )

    assert response.status_code == 201
