def setUp(self):...
test_link = (
    'https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/undead.html#4x4:5,2,4,cRdRLbLbR,2,3,1,3,3,3,1,0,0,1,4,0,0,2,3,1'
    )
board_txt = test_link.split('#')[-1]
board = Board(board_txt)
