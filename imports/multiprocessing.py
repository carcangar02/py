from imports.getArrayNumCaps import getArrayNumCaps
from imports.capBuilder import capBuilder
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

async def multiprocessing(libros):
    """
    Process chapters using multithreading.
    
    Args:
        url (str): The base URL for the chapters.
        name (str): The name of the book.
        num_cap (int): The number of chapters to process.
        
    Returns:
        list: A list of processed chapters.
    """
    libro = libros[0]
    name = libro[0]  # str
    url = libro[1]  # str
    num_cap = libro[2]  # int

    arrayCapitulos = []
    urlCap = url + f'{num_cap}'
    
    # Get the array of chapter numbers
    arrayNumCaps = getArrayNumCaps(urlCap, num_cap)  # OUT: arrayNumCaps[caps] caps(int)
    
    # Prepare arguments for threading
    args = [(url, name, arrayNumCapElement) for arrayNumCapElement in arrayNumCaps]
    
    with ThreadPoolExecutor(max_workers=7) as executor:
        futures = {executor.submit(capBuilder, arg): arg for arg in args}
        
        for future in tqdm(as_completed(futures), total=len(arrayNumCaps)):
            result = future.result(timeout=10)
            arrayCapitulos.append(result)
    
    return arrayCapitulos