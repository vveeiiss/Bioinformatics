def fastq(inp: str):
    return [x for x in inp.replace('\n', '').split('>') if x]