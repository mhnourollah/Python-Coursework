try:
    file_name = input()

    f = open(file_name)

except IOError:
    print("File not found")

finally:
    print("Cleanup complete")
