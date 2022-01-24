stack = []
stack.append(1)
stack.append(2)
stack.append(3)

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()

#O(n)
queue1 = []
queue1.append(1)
queue1.append(2)
queue1.pop(0)

from urllib.request import urlopen
with urlopen('http://blogattach.naver.net/ca5fd665752b2ef2dd3a506a5db3c1b01343b85ee2/20180618_274_blogfile/topspin1278_1529278974170_Fa2424_txt/story.txt') as story:
    story_words = []
    for line in  story:
        line_words = line.decode('utf-8')
        for word in line_words:
            story_words.append(word)


def square(x):
    return x * x

from urllib.request import urlopen


def fetch_words():
    with urlopen('https://suwoni-codelab.com/assets/story.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    for word in story_words:
        print(word)

# __name__ == __main__은 인터프리터에서 직접 실행했을 경우에만 if문 내의 코드를 돌리라는 명령이 됩니다.




