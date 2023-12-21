import csv
from typing import List
import math


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        # Use get_page to retrieve the dataset for the given page
        data = self.get_page(page, page_size)

        # Calculate total pages
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # Calculate next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Create and return the dictionary with hypermedia pagination information
        hyper_data = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return hyper_data


# Example usage:
server = Server()
hyper_data = server.get_hyper(page=2, page_size=5)
print(hyper_data)

