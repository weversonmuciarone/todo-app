import zipfile as zp

def extract_archive(filepath, dest_dir):
    with zp.ZipFile(filepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("compressed.zip", "dest")