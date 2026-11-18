"""  Write make_grid(rows, cols, fill). It returns a list of rows lists, 
each with cols copies of fill, and every row must be an independent list.

Write at least two tests, including one proving that changing grid[0][0] changes only that cell.

Then answer in a comment at the bottom of the file: what happens with make_grid(2, 2, [])
 followed by grid[0][0].append(1)? Is your function still “correct”? Why?
 Predict first, then try it. Commit when it's done.   """


def make_grid(rows, cols, fill):
    grid = []
    for _ in range(rows):
        row = []
        grid.append(row)
        for col in range(cols):
            row.append(fill)
    return grid

def test_changes_link_to_one_cell():
    new_grid = make_grid(2,2,0)
    new_grid[0][0] = 5
    assert new_grid[0][0] != new_grid[1][0]

def test_correct_rows():
    rows = 2
    cols = 2
    fill = 0
    new_grid = make_grid(2,2,0)
    assert len(new_grid) == rows

test_changes_link_to_one_cell()
test_correct_rows()
print("all tests passed")



