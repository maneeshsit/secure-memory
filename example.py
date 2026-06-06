from secure_memory import SecureMemoryStore

memory = SecureMemoryStore()

memory.add_memory(
    "User likes MEMS aerospace systems"
)

memory.add_memory(
    "User works with NVIDIA Orin and ROS2"
)

memory.add_memory(
    "User is building a SWIR AI system"
)

results = memory.search(
    "Tell me about aerospace MEMS"
)

for text, score in results:
    print(f"{score:.4f} : {text}")