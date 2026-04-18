def chunk_text(text, chunk_size=100, overlap=20):
    words = text.split()
    l = len(text)
    chunks = []
    step_size = chunk_size - overlap
    for i in range(0, len(words), step_size):
        chunk = " ".join(words[i : i + chunk_size])
        chunks.append(chunk)
    return chunks
        

    return chunk_list

print(chunk_text("hello i am wasu, i hfa h ga hgihew jig wj iwj fiw fjwi fjweijf ij iwj fijwifj weifjwiej fiwejfiwejf sdnkdnf ksdjfk jsd kfjsdkfj fkds jfksdj fksjdfkjsdfkjsdhs hbfhds fhsdhj fsjhf js fjds fkje kj kjs kjds kjsd kjsd ksd ksd g g  g g g g g  g g g g g g g  g g g g g g g g g g g g g g g g  g g g g g g g g g g g g g g ", 100, 20))
