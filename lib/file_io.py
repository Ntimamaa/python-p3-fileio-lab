def write_file(file_name, file_content):
    file_name = str(file_name)
    with open(file_name + '.txt', 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    file_name = str(file_name)
    with open(file_name + '.txt', 'a') as f:
        f.write(append_content)


def read_file(file_name):
    file_name = str(file_name)
    with open(file_name + '.txt', 'r') as f:
        return f.read()


write_file(file_name="file1", file_content="This is a test content.")
append_file(file_name="file2", append_content="This is a test content.")

print(read_file(file_name="logfile"))

