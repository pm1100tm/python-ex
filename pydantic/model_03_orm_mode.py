""" usage model 03 orm mode
ORM 개체에 매핑되는 모델을 지원하기 위해 임의의 클래스 인스턴스에서 파이던틱 모델을 만들 수 있습니다.
이렇게 하려면: Config 속성 orm_mode를 True로 설정해야 합니다.
모델 인스턴스를 만들려면 from_orm에서 특수 생성자를 사용해야 합니다.
이 예제에서는 SQLLchemy를 사용하지만, 동일한 접근법이 모든 ORM에서 작동해야 합니다.
"""
from typing import List

from pydantic import BaseModel, constr
from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CompanyORM(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=True, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: List[constr(max_length=255)]

    class Config:
        orm_mode = True


if __name__ == '__main__':
    co_orm = CompanyORM(
        id = 123,
        public_key = 'foobar',
        name = 'Testing',
        domains = ['example.com', 'foobar.com']
    )

    print(co_orm)

    co_model = CompanyModel.from_orm(co_orm)
    print(co_model)



