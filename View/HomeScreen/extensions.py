"""
Contains the logic for the game.
---
"""

INITIAL_PLAYER = 'o'

current_player = INITIAL_PLAYER

WINNING_COMBINATIONS = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {1, 4, 7},
    {2, 5, 8},
    {3, 6, 9},
    {1, 5, 9},
    {3, 5, 7},
]

cells_combination = {
    'x' : [],
    'o' : [],
}

def get_current_player(*args) -> list:
    global current_player
    if current_player == 'x':
        text = 'circle-outline'
        current_player = 'o'
    else:
        text = 'close'
        current_player = 'x'
    return text, current_player

def update(id: str, active: bool, *args) -> None:
    global current_player, cells_combination, WINNING_COMBINATIONS

    if active:
        cells_combination[current_player].append(int(id))

    win = any(combination.issubset(cells_combination[current_player]) for combination in WINNING_COMBINATIONS)
    
    if not win and len(cells_combination['x'] + cells_combination['o']) == 9:
        return None
    return win

def reset() -> None:
    global INITIAL_PLAYER, current_player, cells_combination
    current_player = INITIAL_PLAYER
    cells_combination['x'].clear()
    cells_combination['o'].clear()
