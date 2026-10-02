def split_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
):
    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        # Tenta terminar em uma quebra de linha
        if end < len(text):
            newline_position = text.rfind("\n", start, end)

            if newline_position > start:
                end = newline_position

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - overlap

    return chunks