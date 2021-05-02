import os

HEADERS_BYTES = b'\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00'


def remove_headers(filename: str) -> bool:
    """Check if a file contains the HEADERS_BYTES and if so creates a new file without them.
    Then delete the old file and rename the new one as the old.

    :param filename: the path of the file to check / edit.
    :return: True if the file has been edited, False otherwise.
    """
    with open(filename, 'rb') as i:
        if HEADERS_BYTES not in i.read():
            return False

        i.seek(0)

        with open(filename + '.tmp', 'wb+') as o:
            while True:
                data = i.read(16)

                if not data:
                    break

                if HEADERS_BYTES not in data:
                    o.write(data)

    os.remove(filename)
    os.rename(filename + '.tmp', filename)
    print('+', filename)
    return True


def main():
    generator = os.walk(os.getcwd())
    counter = 0

    for t in generator:
        root, _, files = t

        for file in files:
            filename, extension = os.path.splitext(file)

            if extension.lower() in ['.str', '.xa']:
                path = os.path.join(root, file)
                if remove_headers(path):
                    counter += 1

    input(f'Completed - {counter} file(s) edited. Press Enter to exit.')


if __name__ == '__main__':
    main()
