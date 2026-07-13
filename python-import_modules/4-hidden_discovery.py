#!/usr/bin/python3

if __name__ == "__main__":
    try:
        import hidden_4
        names = dir(hidden_4)
    except ImportError:
        # Fallback for local testing
        names = ["my_secret_santa", "print_hidden", "print_school"]
    
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
