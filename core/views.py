from django.shortcuts import render
from random import sample

def kakuro_game(request):
    size = int(request.POST.get("size", 6))

   
    if request.method == "POST" and "new_game" in request.POST or "solution" not in request.session:
        grid = []
        for _ in range(size - 1):
            grid.append(sample(range(1, 10), size - 1))
        request.session["solution"] = grid
    else:
        grid = request.session["solution"]

   
    row_sums = [sum(row) for row in grid]

  
    col_sums = []
    for c in range(len(grid[0])):
        col_total = 0
        for r in range(len(grid)):
            col_total += grid[r][c]
        col_sums.append(col_total)

  
    rows = list(zip(grid, row_sums))

    message = ""

   
    if request.method == "POST" and "check" in request.POST:
        correct = True
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                user_val = request.POST.get(f"cell_{r}_{c}")

                try:
               
                if not user_val or int(user_val) != int(grid[r][c]):
                    correct = False
                    break 
            except ValueError:
              
                correct = False
                break
        if not correct:
            break
                
        message = " Correct!" if correct else " Incorrect solution"

        print(f"Comparing {user_val} to {grid[r][c]}")

    return render(request, "core/kakuro_game.html", {
        "size": size,
        "rows": rows,
        "col_sums": col_sums,
        "message": message
    })