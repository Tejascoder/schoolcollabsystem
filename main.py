from delete_files import delete_files
from delete_files import open_files
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # Execute the open_files function three times concurrently
    for _ in range(3):
        executor.submit(open_files)
        executor.submit(delete_files())