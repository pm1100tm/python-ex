"""
1. shebang 이란?
sharp(#) + bang(!) 합성어
Unix 계열 OS(리눅스, Mac)에서 스크립트(bash, python 등등) 코드 최상단에서 해당 파일을 해석해 줄
인터프리터의 절대경로를 지정

#!인터프리터 절대경로

프로그램의 경로는 시스템에 따라 달라질 수 있습니다.
일반적으로 사용할 수 있는 방법이 /usr/bin/env 파일을 이용하는 방법입니다.

#!/usr/bin/env <언어> 식으로 입력하는 방법이 있습니다.
#!/usr/bin/env bash
#!/usr/bin/env python
#!/usr/bin/env perl
#!/usr/bin/env php

$ which python

words.py 파일 최상단에 아래와 같이 입력하고 저장합니다. 아래의 경로는 저의 시스템 경로입니다.
#!/Users/Blidkaga/.pyenv/shims/python

파일은 저장했지만 한가지가 더 필요합니다. 유닉스 계열환경에서는 실행하도록 권한을 부여해야합니다.
$ chmod +x words.py

./words.py https://suwoni-codelab.com/assets/story.txt

자신의 시스템에서만 사용한다면 이렇게 사용해도 무방합니다.
여러사람이 한 파일을 공유할경우 env를 이용하여 작성하는 것이 좋습니다.
words.py파일에서 env 경로로 작성하고 python을 추가해서 작성해줍니다.
#!/usr/bin/env python
"""
