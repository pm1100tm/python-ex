"""
============usage model 08 helper function
Pydantic은 데이터 구문 분석을 위한 모델에 세 가지 클래스 메소드 도우미 기능을 제공합니다.

*parse_obj
키워드 인수가 아닌 dict를 사용한다는 점을 제외하면 모델의 __init_ 메서드와 매우 유사합니다.
전달된 개체가 딕트가 아닌 경우 ValidationError가 발생합니다.

*parse_raw
문자열 바이트를 json으로 구문 분석한 다음 결과를 parse_obj에 전달합니다.
content_type 인수를 적절하게 설정하여 피클 데이터를 구문 분석할 수도 있습니다.

*parse_file
파일 경로를 가져와 파일을 읽고 내용을 parse_raw 에 전달합니다.
content_type을 생략하면 파일의 확장자에서 추론됩니다.
"""
import pickle
from datetime import datetime
from pathlib  import Path
from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str = 'kim'
    signup_ts: datetime = None


if __name__ == '__main__':
    m = User.parse_obj({'id': 1, 'name': 'lee'})
    print(m)
    # id=1 name='lee' signup_ts=None

    try:
        m = User.parse_obj(['id', 'a', 'test'])
    except ValidationError as e:
        print(e)
        """
        1 validation error for User
        __root__
          User expected dict not list (type=type_error)
        """

    # assumes json as no content type passed
    m = User.parse_raw('{"id": 123, "name": "James"}')
    print(m)
    #> id=123 signup_ts=None name='James'

    pickle_data = pickle.dumps({
        'id'       : 123,
        'name'     : 'James',
        'signup_ts': datetime(2017, 7, 14)
    })

    m = User.parse_raw(pickle_data,
                       content_type='application/pickle',
                       allow_pickle=True)
    print(m)
    #> id=123 signup_ts=datetime.datetime(2017, 7, 14, 0, 0) name='James'

    path = Path('data.json')
    path.write_text('{"id": 123, "name": "James"}')
    m = User.parse_file(path)
    print(m)
    #> id=123 signup_ts=None name='James'
