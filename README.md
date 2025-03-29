# PyChunkCore

## Overview
**PyChunkCore** is an advanced chunk-processing module that serves as a **drop-in replacement** for Python's deprecated `chunk` module. It extends the functionality by integrating `pychunk`, making it compatible with legacy and modern systems.

### Key Features
✅ Fully compatible with Python 3.12 and 3.13+  
✅ Implements both `chunk` and `pychunk` in a unified package  
✅ Supports **big-endian** and **little-endian** file parsing  
✅ Provides enhanced performance and additional utilities  
✅ Acts as a seamless bridge for `aifc` and other legacy modules

---
## Installation
Install via **pip**:
```sh
pip install pychunkcore
```

Or install from source:
```sh
git clone https://github.com/your-username/PyChunkCore.git
cd PyChunkCore
pip install .
```

---
## Usage
### Basic Example
```python
from pyaifchunk.core_chunk import Chunk

with open("example.wav", "rb") as file:
    chunk = Chunk(file)
    print("Chunk Name:", chunk.getname())
    print("Chunk Size:", chunk.getsize())
    data = chunk.read()
    chunk.close()
```

### Handling AIFF Files (`aifc` Module Compatibility)
```python
from pyaifchunk.core_aifc import open # PyChunkCore ensures aifc works properly

with aifc.open("example.aiff", "rb") as af:
    print("Audio Params:", af.getparams())
    print("Sample Width:", af.getsampwidth())
```

---
## Compatibility
PyChunkCore is designed to work with **Python 3.12+**, ensuring compatibility with modules like `aifc` that previously relied on `chunk`.

### Supported Platforms
✅ Windows  
✅ Linux  
✅ macOS  

---
## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-new`.
3. Make your changes and commit: `git commit -m "Added new feature"`.
4. Push to the branch: `git push origin feature-new`.
5. Submit a pull request!

---
## License
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
  See the LICENSE file for more details. See the [LICENSE](LICENSE) file for details.

---
## Contact
📧 Email: swskye17@gmail.com  
🐍 GitHub: [skye](https://github.com/skye-waves/PyChunkCore)

