from chunk import Chunk
import io
# Helper function to create a chunk binary block

def create_chunk(chunk_id: bytes, data: bytes, bigendian: bool = True, inclheader: bool = False, align: bool = True) -> bytes:
    """
    Constructs a binary chunk:
      - chunk_id: 4-byte identifier (must be exactly 4 bytes)
      - data: bytes of the chunk's data
      - If inclheader is True, the size field includes the 8-byte header.
      - If align is True and the data length is odd, a pad byte (b'\x00') is appended.
    """
    if len(chunk_id) != 4:
        raise ValueError("Chunk ID must be exactly 4 bytes")
    data_size = len(data)
    if inclheader:
        size_value = data_size + 8
    else:
        size_value = data_size
    size_bytes = size_value.to_bytes(
        4, byteorder='big' if bigendian else 'little')
    header = chunk_id + size_bytes
    # Append pad byte if needed
    pad = b'\x00' if align and (data_size % 2 != 0) else b''
    return header + data + pad


# Create two test chunks:
# Chunk 1: Even data length (10 bytes), no pad byte expected.
chunk1 = create_chunk(b'CHNK', b'0123456789', inclheader=False)
# Chunk 2: Odd data length (7 bytes), pad byte expected.
chunk2 = create_chunk(b'ODDY', b'ABCDEFG', inclheader=False)

# Concatenate chunks into one binary stream
binary_stream = io.BytesIO(chunk1 + chunk2)

# Import our Chunk class (assuming the implementation is in a file named chunk.py)

# --- Test Chunk 1 ---
print("=== Testing Chunk 1 ===")
# Create a Chunk instance for the first chunk
c1 = Chunk(binary_stream, align=True, bigendian=True, inclheader=False)

# Verify chunk ID
print("Chunk 1 ID:", c1.getname())      # Expected: b'CHNK'
# Verify data size
print("Chunk 1 Data Size:", c1.getsize())  # Expected: 10
# Read all data from chunk 1
data1 = c1.read()
print("Chunk 1 Data:", data1)           # Expected: b'0123456789'
# Subsequent read should return empty bytes
print("Chunk 1 Read after EOF:", c1.read())

# --- Test Chunk 2 ---
print("\n=== Testing Chunk 2 ===")
# Now, binary_stream is positioned at the start of chunk2.
c2 = Chunk(binary_stream, align=True, bigendian=True, inclheader=False)
print("Chunk 2 ID:", c2.getname())      # Expected: b'ODDY'
print("Chunk 2 Data Size:", c2.getsize())  # Expected: 7

# Read first 4 bytes of chunk2
data2_part = c2.read(4)
print("Chunk 2 Partial Read (4 bytes):", data2_part)  # Expected: b'ABCD'
# Current position in chunk2
print("Chunk 2 current position (tell):", c2.tell())

# Seek back to start of chunk2 data
c2.seek(0)
# Read all data from chunk2
data2_all = c2.read()
print("Chunk 2 Full Data:", data2_all)  # Expected: b'ABCDEFG'
# (Note: The pad byte is not returned by read() because we only consider the data size)

# --- Test skip() functionality ---
print("\n=== Testing skip() ===")
# Reset stream to beginning
binary_stream.seek(0)
# Create a new Chunk instance for chunk1 and immediately skip it.
c1_skip = Chunk(binary_stream, align=True, bigendian=True, inclheader=False)
c1_skip.skip()
pos_after_c1 = binary_stream.tell()
# For chunk1, header (8 bytes) + data (10 bytes) = 18 bytes; no pad since 10 is even.
# Expected: 18 (the start of chunk2)
print("Stream position after skipping Chunk 1:", pos_after_c1)

print("\nAll tests completed.")
