with open("file.txt", "w") as f:
    for i in range(1, 6):
        f.write(f"This is line {i}\n")
with open("file.txt", "a") as f:
    f.write("This is line 6\n")
    f.write("This is line 7\n")
