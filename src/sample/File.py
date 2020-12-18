import os


class File:

    def read_file(self, file):
        with open(file, 'r') as f:
            content = f.read()
        return content

    def write_file(self, file, data):
        with open(file, 'w') as f:
            f.write(data)

    def delete_file(self, file):
        if os.path.isfile(file):
            os.remove(file)
        else:
            raise(Exception, 'File not found')
