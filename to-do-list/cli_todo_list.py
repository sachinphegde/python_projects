#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple command-line to-do list application.
"""
import argparse
import os
import json

TO_DO_LIST_FILE = "todo_list.json"

def load_todo_list():
    if not os.path.exists(TO_DO_LIST_FILE):
        with open(TO_DO_LIST_FILE, "w", encoding= "UTF-8") as file:
            file.write("[]")

    with open(TO_DO_LIST_FILE, "r", encoding="UTF-8") as file:
        try:
            todo_list = json.load(file)
        except json.JSONDecodeError:
            todo_list = []
    return todo_list


def get_user_input():
    """
    Parses command-line arguments for the to-do list application.
    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="A simple command-line to-do list application.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Action to perform")
    # add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="Task to add")
    # delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")
    # modify task
    modify_parser = subparsers.add_parser("modify", help="Modify a task")
    modify_parser.add_argument("task_id", type=int, help="ID of the task to modify")
    modify_parser.add_argument("new_task", help="New task description")
    # list task
    list_parser = subparsers.add_parser("list", help="List all tasks")
    group = list_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="List all tasks")
    group.add_argument("--done", action="store_true", help="List completed tasks")
    group.add_argument("--todo", action="store_true", help="List pending tasks")
    group.add_argument("--in-progress", action="store_true", help="List tasks with progress")
    #update task progress
    progress_parser = subparsers.add_parser("progress", help="Update task progress")
    progress_parser.add_argument("task_id", type=int, help="ID of the task to update progress")
    group = progress_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--todo", action="store_true", help="List pending tasks")
    group.add_argument("--done", action="store_true", help="List completed tasks")
    group.add_argument("--in-progress", action="store_true", help="List tasks with progress")

    args = parser.parse_args()
    return args

# def add_task():
    
# def delete_task():
    
# def update_task():
    
# def list_task():
    
# def task_progress():
    
def main():
    try:
        args = get_user_input()
    except SystemExit as e:
        exit(e.code)


if __name__ == "__main__":
    main()
