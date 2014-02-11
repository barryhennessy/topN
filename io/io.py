__author__ = 'barryhennessy'


class IO(object):
    """Handles IO for TopN."""

    def read(self, path):
        """Reads integers from the path given with a generator

        :param path: The path to the file to be read

        :return: Generator of ints
        """
        with open(path, "rU") as input_file:
            for line in input_file:
                current_int = int(line)
                yield current_int