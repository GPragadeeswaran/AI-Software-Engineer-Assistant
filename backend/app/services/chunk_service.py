class ChunkService:

    def create_chunks(self, files: list, chunk_size: int = 5):

        chunks = []

        for i in range(0, len(files), chunk_size):

            chunk = files[i:i + chunk_size]

            chunks.append(chunk)

        return chunks