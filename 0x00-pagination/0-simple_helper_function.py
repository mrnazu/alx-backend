def index_range(page, page_size):
    # Adjust page number to be 0-indexed
    adjusted_page = page - 1

    # Calculate start and end indexes based on pagination parameters
    start_index = adjusted_page * page_size
    end_index = start_index + page_size - 1

    # Return a tuple of start and end indexes
    return start_index, end_index

# Example usage:
page = 3
page_size = 10
start_index, end_index = index_range(page, page_size)

print(f"Start Index: {start_index}, End Index: {end_index}")

