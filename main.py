"""Minimal terminal task manager: add, list, complete, and remove tasks (in-memory)."""

tasks = []

def show():
    if not tasks:
        print("No tasks.")
        return
    for i, (text, done) in enumerate(tasks, 1):
        print(f"{i:>3}. [{'x' if done else ' '}] {text}")

def main():
    print("Commands: add <text> | list | done <n> | rm <n> | quit")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        cmd, _, arg = line.partition(" ")
        cmd = cmd.lower()
        if cmd in ("quit", "exit", "q"):
            break
        elif cmd == "add":
            if arg:
                tasks.append((arg, False))
            else:
                print("Usage: add <text>")
        elif cmd == "list":
            show()
        elif cmd == "done":
            try:
                i = int(arg) - 1
                tasks[i] = (tasks[i][0], True)
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif cmd == "rm":
            try:
                tasks.pop(int(arg) - 1)
            except (ValueError, IndexError):
                print("Invalid task number.")
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()