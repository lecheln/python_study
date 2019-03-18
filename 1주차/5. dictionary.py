# dictionary, 즉 사전이라고 불리는 자료형입니다.
# 이 자료형은 c++의 map과 동일합니다.
# 키값은 수정이 불가능합니다.
# {key1 : value1, key2 : value2, key2 : value2}
dic = {'name':'hi', 'phone':'01000000000', 'birth': '1002'}
a = { 'a': [1,2,3]}
dic = dict()        # 빈 사전형 정의

# 사전에 데이터 추가하기
a = {1:'a'}
a[2] = 'b'              # {1: 'a', 2: 'b'}
a['name'] = 'pey'       # {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1,2,3]          # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
del a[1]                # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 키값 리스트를 가져오는법
a = {'name':'hi', 'phone':'01000000000', 'birth': '1002'}
a.keys()                # dict_keys(['name','phone','birth']) , 
                        # dict_keys는 list와 동일하지만, 리스트이 함수를 사용할 수 없어서, list로 변환해서 사용합니다.
list(a.keys())          # change dict_keys to list

# 값 리스트를 가져오는법
a = {'name':'hi', 'phone':'01000000000', 'birth': '1002'}
a.values()              # dict_values(['hi','01000000000','1002'])

# 모든 아이템을 가져오는방법
a.items()               # dict_items([('name', 'hi'), ('phone', '0119993323'), ('birth', '1118')])

# 전부다 지우기
a.clear()               # {}

# 키값으로 값을 가져오는 방법
# get()함수나 인덱싱으로 가져올수 있다.
# 인덱싱으로 가져오는 경우 키값이 존재하지 않으면 error가 뜨지만
# get으로 가져오면 키값이 없는경우, 반환할 메세지를 정할 수 있다.
a = {'name':'hi', 'phone':'01000000000', 'birth': '1002'}
a.get('name')           # 'hi'
a['name']               # 'hi'
a['test']               # error
a.get('test')           # return None
a.get('test', 'error')  # 'error'

# 키가 있는지 확인하는 방법
'name' in a             # true