""" usage model 04 reserved names
필드 별칭(alias) 를 지정할 수 있다.
"""
import typing

from pydantic import BaseModel, Field
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


class MyModel(BaseModel):
    metadata: typing.Dict[str, str] = Field(alias='metadata_')

    class Config:
        orm_mode = True


BaseModel = declarative_base()


class SQLModel(BaseModel):
    __tablename__ = 'my_table'
    id = sa.Column('id', sa.Integer, primary_key=True)
    # 'metadata' is reserved by SQLAlchemy, hence the '_'
    metadata_ = sa.Column('metadata', sa.JSON)


if __name__ == '__main__':
    sql_model = SQLModel(metadata_ = {'key': 'val'}, id = 1)
    pydantic_model: MyModel = MyModel.from_orm(sql_model)

    print(pydantic_model.dict())
    # {'metadata': {'key': 'val'}}

    print(pydantic_model.dict(by_alias=True))
    # {'metadata_': {'key': 'val'}}
