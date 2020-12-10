class Shape:
    cat = 'Geometrical Shapes'

    def __init__(self, type1):
        self.typ = type1

    def show(self):
        print('Shape is of category: ', Shape.cat)
        print('And shape is: ', self.typ)


tr = Shape('Triangle')
sq = Shape('Square')
rec = Shape('Circle')

tr.show()
sq.show()
rec.show()
