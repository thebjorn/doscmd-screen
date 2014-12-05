# -*- coding: utf-8 -*-

from screen import Screen

def _pause(scr):
    scr.gotoxy(10, 10)
    raw_input('')


def test_screen_layout(s):
    s.writexy(s.left, s.top, 'left top')
    #_pause(s)
    s.writexy(s.left, s.bottom, 'left bottom')
    #_pause(s)
    s.rightxy(s.right, s.bottom, 'right bottom')
    #_pause(s)
    s.rightxy(s.right, s.top, 'right top')
    #_pause(s)

    x = 2; y = 2
    s.writelinesxy(x, y, s.coords)


def test_height(s):
    x = s.center
    for y in range(s.height):
        s.rightxy(x, y, y)
        s.writexy(x, y, '|', y)


def test_width(s):
    def dotpos(x, y):
        s.writexy(x, y, '.')
        txt = str(x)
        if x + len(txt) > s.right:
            s.rightxy(x, y+1, x)
        else:
            s.writexy(x, y+1, x)

    for x in range(s.width):
        s.writexy(x, s.middle, '=')

    y = s.middle + 3
    for x in range(0, s.width, 5):
        dotpos(x, y)

    
def print_colors(s):
    """Print the color palette to screen.
    """
    startx = 4
    starty = 4
    colwidth = 20
    colheight = len(s.colors) + 1
    cols = (s.width - startx) // colwidth
    col = row = 0
    x = startx
    y = starty
    
    for b, bg in enumerate(s.colors):
        x = col * colwidth + startx
        if x + colwidth > s.right:
            x = startx
            col = 0
            row += 1
        col += 1

        for f, fg in enumerate(s.colors):
            s.writexy(
                x, starty + row * colheight + f,
                ("%s on %s" % (fg, bg)).ljust(colwidth - 1),
                fg=fg, bg=bg
            )


def test_colorstr(s):
    s.gotoxy(5, 20)
    print colorstr('hello', 'red', 'black')
    s.gotoxy(5, 21)
    print colorstr('hello', 'black', 'red')


def test_middle_center(s):
    s.centerxy(s.center, s.middle, '((.))')
    s.centerxy(s.center, s.middle-1, 'centered, and')
    s.centerxy(s.center, s.middle+1, 'in the middle')

if __name__ == "__main__":
    s = Screen(fg='white', bg='black')

    s.cls()                             
    test_height(s)
    test_width(s)
    test_screen_layout(s)
    print_colors(s)
    test_middle_center(s)
    _pause(s)
