# -*- coding: utf-8 -*-
import time

from screen import Screen, Window


def main():
    s = Screen(fg='white', bg='black')
    s.cls('green')
    w = Window(s, 5, 5, 25, 10)
    w.cls()

    # for i in range(10):
    #     print >>w, i

    w2 = Window(s, 66, 5, 120, 10)
    w2.cls()

    # for i in range(31):
    #     print >>w, 'a' * i
    #     time.sleep(0.4)
    #
    # print >>w, 'abcdefghi\njklmnopqrstuvwxyz'
    # print >>w, 'abcdefghijklmnopqrstuvwxyz'
    # print >>w, 'HI'

    print >>w, open(__file__).read()

    # print >>w2, 'world'
    # print >>w2, 'YO'

    s.gotoxy(s.left, s.bottom)
    # print w.dbg
    # print
    # print w.content

if __name__ == '__main__':
    main()
