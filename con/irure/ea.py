def loop():
    """Loops until a condition is met."""
    while True:
        action = input("Enter 'exit' to stop the loop: ")
        if action == 'exit':
            print("Exiting loop.")
            break
        else:
            # Perform some action here
            pass
