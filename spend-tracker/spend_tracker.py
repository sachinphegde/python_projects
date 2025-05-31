#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple command-line spend tracker application.
"""
import argparse
import os
import sys
import sqlite3
import datetime
from pathlib import Path
import dateutil.parser
import matplotlib

# Constants
# OS	| Path.home() points to
# ------|----------------------
# Linux	| /home/username
# macOS	| /Users/username
# Windows | C:\Users\username
homedir = Path.home()
EXPENSE_DB = homedir/"spend_tracker.db"


def create_database():
    """
    Creates the database and the expenses table if it does not exist.
    """
    conn = sqlite3.connect(EXPENSE_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            subCategory TEXT,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def get_user_args():
    """
    Parses command-line arguments for the spend tracker application.
    """
    parser = argparse.ArgumentParser(description="A simple command-line spend tracker application.")
    subparsers = parser.add_subparsers(dest='command')

    # add_expense
    subparsers.add_parser('add', help='Add a new expense')

    # view_expenses
    view_parser = subparsers.add_parser('view', help='View all expenses')
    view_parser.add_argument()

    args = parser.parse_args()
    return args


def add_expense():
    """
    Adds a new expense to the database.
    """
    expense_date = input("Enter date (dd-mm-yyyy) or press Enter for today: ").strip()
    if not expense_date:
        expense_date = datetime.datetime.now().strftime("%d-%m-%Y")
    print(f"adding expense for {expense_date}. Enter q to quit.")

    while True:
        amount = input("Amount (or 'q' to quit): ").strip()
        if amount == 'q':
            break
        description = input("Description: ").strip()
        category = input("Category: ").strip()
        sub_category = input("Sub Category: ").strip()
        if not amount or not category:
            print("Amount and category are required.")
            continue
        conn = sqlite3.connect(EXPENSE_DB)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO expenses (
            description, amount, category, subCategory, date)
            VALUES (?, ?, ?, ?)
            """,
            (description, float(amount), category, sub_category, expense_date)
        )
        conn.commit()
        conn.close()
        print("Expsense added.\n")


def get_expense_sum():
    """
    Calculates the total sum of expenses in the database.
    """
    conn = sqlite3.connect(EXPENSE_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_sum = cursor.fetchone()[0]
    conn.close()
    return total_sum if total_sum is not None else 0.0


def view_expenses(args):
    """
    Views all expenses in the database.
    """
    conn = sqlite3.connect(EXPENSE_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date = ?", (date_str,))

    conn.commit()
    conn.close()


def delete_expense(args):
    """
    Deletes an expense from the database.
    """
    conn = sqlite3.connect(EXPENSE_DB)
    cursor = conn.cursor()

    conn.commit()
    conn.close()


def stats_graph(args):
    """
    Generates statistics or a graph based on the expenses.
    """
    conn = sqlite3.connect(EXPENSE_DB)
    cursor = conn.cursor()

    conn.commit()
    conn.close()


def main():
    """
    Main function to run the spend tracker application.
    """
    if not os.path.exists(EXPENSE_DB):
        create_database()

    try:
        args = get_user_args()
    except SystemExit as error:
        sys.exit(error.code)

    if args.command == "add":
        add_expense()
    elif args.command == "view":
        view_expenses(args)
    elif args.command == "stats":
        stats_graph(args)


if __name__ == "__main__":
    main()
