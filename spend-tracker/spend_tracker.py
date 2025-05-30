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
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()


def get_user_args():

    

def add_expense(args):
    

def view_expenses(args):
    

def delete_expense(args):
    

def list_expenses(args):
    

def stats_graph(args):

def main():
    conn = sqlite3.connect(EXPENSE_DB)
    curser = conn.cursor()

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()