#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col) without conflict.

    Args:
        board (list): Current placement, board[i] = column of queen in row i.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        True if placing a queen here is safe, False otherwise.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n):
    """Find all solutions to the N queens puzzle.

    Args:
        n (int): The size of the board.

    Returns:
        A list of solutions, each a list of [row, col] pairs.
    """
    solutions = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            solution = [[r, board[r]] for r in range(n)]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


def main():
    """Parse arguments and print all N queens solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in solve_nqueens(n):
        print(solution)


if __name__ == "__main__":
    main()
