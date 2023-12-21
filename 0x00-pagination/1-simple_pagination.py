import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    # Adjust page number to be 0-indexed
    adjusted_page = page - 1

    # Calculate start and end indexes based on pagination parameters
    start_index = adjusted_page * page_size
    end_index = start_index + page_size - 1

    # Return a tuple of start and end indexes
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Check if the indexes are out of range for the dataset
        if start_index >= len(dataset):
            return []

        # Return the appropriate page of the dataset
        return dataset[start_index:end_index + 1]


# Example usage:
server = Server()
page_data = server.get_page(page=2, page_size=5)
print(page_data)

