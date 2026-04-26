def read_file(filename):
    with open(filename, "rb") as f:
        return f.read()

def save_file(filename, data):
    with open("received_" + filename, "wb") as f:
        f.write(data)