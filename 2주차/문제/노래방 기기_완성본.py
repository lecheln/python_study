import pickle

# Default
coin = 0
reservation = []
karaoke = []
FLAG = True

# Setting
CONFIG = {
    'PATH'  : "E:\\music.txt" ,
    'Error' : '[경고] 잘못된 명령어 입니다.',
    'cost'  : 500, 
    'count' : 2,
    'format': '{0:^60}',
    'title' : '\n\n{0}({1}곡)\n',
    'coin'  : '{0}원에 {1}곡\n',
    'input' : '\n>> '
}

COMMAND = {
    'search' : {
        'cmd' : {
            'no'        : '번호', 
            'title'     : '제목', 
            'singer'    : '가수'
        }, 
        'Error'         : '[경고] 잘못된 명령어 입니다', 
        'function'      : 'searchFunc',
        'Explanation'   : 'search (title/singer/no) 키워드 : 검색',
        'default'       : 'title',
        'successMsg'    : '[안내] {0}이/가 \'{1}\'인 곡 리스트 입니다\n',
        'failMsg'       : '[안내] {0}이/가 \'{1}\'인 곡은 없습니다\n'
    },
    'print' : {
        'cmd' : {
            'rank' : {
                'name'  : '랭킹차트', 
                'arr'   : 'karaoke', 
                'type'  : True, 
                'print' : '순위 번호 제목 가수',
                'format': '{rank} {0} {1}-{2}'
            },
            'book' : {
                'name'  : '예약목록',
                'arr'   : 'reservation', 
                'type'  : False, 
                'print' : '번호 제목 가수',
                'format': '{0} {1}-{2}',
                'book'  : '[{0}] {1} - {2} 예약되었습니다. ({3}곡)'
            },
        },
        'Error'         : '[경고] 잘못된 명령어 입니다',
        'Explanation'   : 'print (rank/book): 순위/예약곡 보기',
        'function'      : 'printFunc',
        'default'       : 'rank',
        'successMsg'    : '{0} 입니다 {1}곡\n'
    },
    'insert' : {
        'costError'     : '[경고] 잘못된 값입니다.', 
        'Error'         : '[경고] 잘못된 명령어 입니다', 
        'Explanation'   : 'insert 숫자 : 코인 입력',
        'function'      : 'insertFunc',
        'successMsg'    : '[안내] {0}곡이 입력되었습니다.'
    },
    'reservation' : {
        'arr'           : 'reservation', 
        'coinError'     : '[경고] 코인이 없습니다.', 
        'Error'         : '[경고] 잘못된 명령어 입니다.', 
        'Explanation'   : '숫자입력 : 예약하기',
        'function'      : 'reservationFunc' 
    },
    'exit' : {
        'msg'           : '[안내] 시스템을 종료합니다.', 
        'Explanation'   : 'exit : 종료하기',
        'function'      : 'exitFunc'
    }
}


def exitFunc(com, cmdConfig):
    global FLAG
    print(cmdConfig['msg'])
    FLAG = False
    
def printMessage():
    print(CONFIG['title'].format('=' * 60, coin))
    print(CONFIG['format'].format(CONFIG['coin'].format(CONFIG['cost'], CONFIG['count'])))
    for key in list(COMMAND.values()):
        print(CONFIG['format'].format(key['Explanation']))
    return input(CONFIG['input']).lower().split()

def printFormat(sing, isRank = "book", isBook = False):
    command = COMMAND['print']['cmd']
    if isBook:
        print(command['book']['book'].format(sing['no'], sing['title'], sing['singer'], coin))
    else :
        print(command[isRank]['format'].format(sing['no'], sing['title'], sing['singer'], rank = sing['rank']))

def printFunc(input_str, cmdConfig):
    if len(input_str) :
        command = input_str[0]
    else:
        command = cmdConfig['default']
        
    if cmdConfig['cmd'].get(command):
        printtext = cmdConfig['cmd'][command]
        printlist = eval(printtext['arr'])
        print(cmdConfig['successMsg'].format(printtext['name'], len(printlist)))
        if len(printlist) > 0:
            print(printtext['print'])
            for li in printlist:
                printFormat(li, command)
    else:
        print(cmdConfig['Error'])
        
def searchFunc(find_type, cmdConfig):
    if len(find_type) > 1:
        command = find_type[0]
        del find_type[0]
    else:
        command = cmdConfig['default']

    search = ' '.join(find_type).lower()
    
    if cmdConfig['cmd'].get(command) :
        sing = list(filter(lambda x : str(x[command]).lower() == search, karaoke))
        if len(sing):
            print(cmdConfig['successMsg'].format(cmdConfig['cmd'][command], search.upper()))
            for li in sing:
                printFormat(li)
        else:
            print(cmdConfig['failMsg'].format(cmdConfig['cmd'][command], search.upper()))
    else :
        print(cmdConfig['Error'])

def insertFunc(cmd, cmdConfig):
    input_coin = ""
    if len(cmd) :
        input_coin = cmd[0]
        
    if input_coin.isnumeric():
        coin_val = int(input_coin)
        if coin_val % CONFIG['cost'] == 0 and coin_val > 0:
            global coin
            coin = coin + (coin_val // CONFIG['cost'] * CONFIG['count'])
            print(cmdConfig['successMsg'].format(coin_val // CONFIG['cost'] * CONFIG['count']))
        else:
            print(cmdConfig['costError'])
    else: 
        print(cmdConfig['Error'])

def reservationFunc(num, cmdConfig):
    if isinstance(num, list):
        num = num[0]
    if num.isnumeric():
        sing = list(filter(lambda x : x['no'] == int(num[-5:]), karaoke))
        
        if len(sing):
            global coin
            if coin > 0:
                coin = coin - 1
                printFormat(sing[0], isBook = True)
                eval(cmdConfig['arr']).append(sing[0])
            else:
                print(cmdConfig['coinError'])
        else:
            print(cmdConfig['Error'])
    else:
        print(cmdConfig['Error'])

def doMain():
    while FLAG:
        cmdLine = printMessage()
        cmd = cmdLine[0]
        del cmdLine[0]
        if cmd.isnumeric():
            reservationFunc(cmd, COMMAND['reservation'])
        elif COMMAND.get(cmd):
            eval(COMMAND[cmd]['function'])(cmdLine, COMMAND[cmd])
        else:
            print(CONFIG['Error'])

if __name__ == "__main__":
    with open(CONFIG['PATH'], 'rb') as f:
        karaoke = pickle.load(f)
    doMain()
