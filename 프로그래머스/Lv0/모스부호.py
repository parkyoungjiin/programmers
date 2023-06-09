"""머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다. 
그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다. 
문자열 letter가 매개변수로 주어질 때, 
letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
모스부호는 다음과 같습니다.
- 모스부호는 공백을 기준으로 나누어져있음.
    - letter에서 공백을 찾아서 split해야 할 것 같음.
- 모스부호 = 딕셔너리로 되어있음.
- letter라는 문자열을 배열로 담아?

"""

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    answer = ''
    # 공백 기준으로 분리.
    arr = letter.split()
    print(arr)
    # For -> arr 에 있는 부호들 하나하나가 dict에 존재하는 지 판별
    for i in arr:
        for key, value in morse.items():
            if i == key:
                answer += value
    
    return answer

def solution2(letter):
    answer = ''

    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }   
    # split으로 공백 기준으로 분리함.)
    letter_arr = letter.split()
    # 분리한 배열을 dict[키] = 값 문법을 통해서 풀이함.
    for i in letter_arr:
        answer += morse[i]
    return print('정답:', answer)
def solution3(letter):
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }   
    return print(''.join([morse[i] for i in letter.split()]))

solution(".... . .-.. .-.. ---")
solution2(".... . .-.. .-.. ---")
solution3(".... . .-.. .-.. ---")