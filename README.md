# secure-memory
A proof-of-concept for a privacy-preserving AI memory system where vector memories remain encrypted at rest, in transit, and during computation.

Microsoft SEAL—powered by open-source homomorphic encryption technology—provides a set of encryption libraries that allow computations to be performed directly on encrypted data. This enables software engineers to build end-to-end encrypted data storage and computation services where the customer never needs to share their key with the service.

Microsoft SEAL is open source (MIT license).
# Install tenseal
pip install tenseal numpy sentence-transformers
# run the code
python secure_memory.py
# run the code
python example.py
# Display the Output
<img width="442" height="72" alt="image" src="https://github.com/user-attachments/assets/c21a112a-ea9e-4159-901b-9c595809339e" />

