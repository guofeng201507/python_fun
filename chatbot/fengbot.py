# fengbot.py
from nltk.chat.util import Chat, reflections

pairs = [
    (
        r'hi',
        ['hello', 'kamusta', 'mabuhay', ]
    ),

    (
        r'Which stock',
        ['tencent', 'Alibaba']
    )
]


def hugot_bot():
    print("Hi how can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    hugot_bot()
