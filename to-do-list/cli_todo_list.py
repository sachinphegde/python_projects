#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple command-line to-do list application.
"""
import argparse
import os
import json
import datetime

# Constants
TO_DO_LIST_FILE = "todo_list.json"

def load_todo_json():
    """
    Loads the to-do list from a JSON file.
    If the file does not exist, it creates an empty list.
    If the file is empty or contains invalid JSON, it initializes an empty list.
    If the file is not empty, it loads the JSON data into a list.
    If the file is not valid JSON, it initializes an empty list.

    Returns:
        list: A list of tasks loaded from the JSON file.
    """
    if not os.path.exists(TO_DO_LIST_FILE):
        with open(TO_DO_LIST_FILE, "r+", encoding= "UTF-8") as file:
            file.write("[]")
            todo_list = json.load(file)
    else:
        with open(TO_DO_LIST_FILE, "r+", encoding="UTF-8") as file:
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

def add_task(task_desc):
    """
    Adds a new task to the to-do list.
    """
    todo_list = load_todo_json()
    max_id = max((task.get("id", 0) for task in todo_list), default=0)
    new_id = max_id + 1
    created_at = datetime.datetime.now().isoformat()
    updated_at = created_at  # Initially, created and updated timestamps are the same
    # Create a new task dictionary
    new_task = {
        "id": new_id,
        "task": task_desc,
        "status": "todo",
        "created_at": created_at,
        "updated_at": updated_at
        }
    todo_list.append(new_task)
    with open(TO_DO_LIST_FILE, "w", encoding="UTF-8") as file:
        json.dump(todo_list, file, indent=2, ensure_ascii=False)

def delete_task(id):
    """
    Deletes a task from the to-do list by its ID.
    """
    todo_list = load_todo_json()

    with open(TO_DO_LIST_FILE, "w", encoding="UTF-8") as file:
        json.dump(todo_list, file, indent=2, ensure_ascii=False)

def update_task():
    print("Update task")

def list_task(args):
    """
    Lists tasks based on the specified type.
    """
    todo_list = load_todo_json()
    for task in todo_list:
        if args.all:
            print(f"ID: {task['id']} | Task: {task['task']} | Status: {task['status']}")
        elif args.todo and task['status'] == "todo":
            print(f"ID: {task['id']} | Task: {task['task']} | Status: {task['status']}")
        elif args.done and task['status'] == "done":
            print(f"ID: {task['id']} | Task: {task['task']} | Status: {task['status']}")
        elif args.in_progress and task['status'] == "in-progress":
            print(f"ID: {task['id']} | Task: {task['task']} | Status: {task['status']}")


def task_progress():
    """
    Updates the progress of a task.
    """
    print("Update task progress")


def main():
    """
    Main function to run the command-line to-do list application.
    """
    try:
        args = get_user_input()
    except SystemExit as e:
        exit(e.code)

    if args.command == "add":
        add_task(args.task)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "modify":
        update_task(args.task_id, args.new_task)
    elif args.command == "list":
        list_task(args)

if __name__ == "__main__":
    main()
