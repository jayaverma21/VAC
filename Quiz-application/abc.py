import threading

def task():
    print("Executing task...")

# Create multiple threads
threads = []
for _ in range(5):
    t = threading.Thread(target=task)
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

print("All tasks completed.")