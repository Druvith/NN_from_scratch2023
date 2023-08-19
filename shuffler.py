import os
import random

def shuffle_chunk(chunk_path, seed, chunk_size):
    # Read the chunk data
    with open(chunk_path, 'r') as file:
        data = file.readlines()

    # Shuffle the data using a pseudorandom permutation generator
    random.Random(seed).shuffle(data)

    # Write the shuffled data back to the chunk file
    with open(chunk_path, 'w') as file:
        file.writelines(data)

def shuffle_data_on_disk(chunks_dir, chunk_size, seed):
    # List all chunk files
    chunk_files = [os.path.join(chunks_dir, f) for f in os.listdir(chunks_dir) if os.path.isfile(os.path.join(chunks_dir, f))]

    # Shuffle the data within each chunk
    for i, chunk_file in enumerate(chunk_files):
        shuffle_chunk(chunk_file, seed + i, chunk_size)

    # Generate a global permutation for the chunks using the same seed
    global_permutation = list(range(len(chunk_files)))
    random.Random(seed).shuffle(global_permutation)

    # Access the shuffled chunks in the globally shuffled order
    for chunk_index in global_permutation:
        chunk_file = chunk_files[chunk_index]
        # Process the shuffled chunk (e.g., read it for training)
        # ...

# Example usage
chunks_dir = 'path/to/chunks'
chunk_size = 1000
seed = 42

shuffle_data_on_disk(chunks_dir, chunk_size, seed)

