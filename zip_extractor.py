import zipfile

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, "r") as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("/Users/leaveiljohnson/Documents/Python Projects/ZipExtractor/Leaveil Johnson CV.pdf.zip",
                    "/Users/leaveiljohnson/Documents/Python Projects/ZipExtractor")