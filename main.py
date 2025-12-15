import json
import os
import urllib.request
from pathlib import Path
from typing import Dict, List


class SnapchatMemoryDownloader:
    """Downloads Snapchat memories from a JSON export file."""

    def __init__(self, json_file: str, output_dir: str):
        self.json_file = Path(json_file)
        self.output_dir = Path(output_dir)
        self.stats = {"downloaded": 0, "skipped": 0, "failed": 0}

    def run(self):
        """Main execution method."""
        self._validate_inputs()
        self._ensure_output_dir()

        media_items = self._load_media_items()
        existing_files = self._get_existing_files()

        print(f"Found {len(media_items)} media items in JSON file")
        print(f"Starting download process...\n")

        self._download_media(media_items, existing_files)
        self._print_summary()

    def _validate_inputs(self):
        """Validate that the JSON file exists."""
        if not self.json_file.exists():
            raise FileNotFoundError(f"JSON file not found: {self.json_file}")

    def _ensure_output_dir(self):
        """Create output directory if it doesn't exist."""
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _load_media_items(self) -> List[Dict]:
        """Load media items from JSON file."""
        try:
            with open(self.json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data.get("Saved Media", [])
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON file: {e}")

    def _get_existing_files(self) -> set:
        """Get set of existing files in output directory."""
        return set(f.name for f in self.output_dir.iterdir() if f.is_file())

    def _get_file_extension(self, media_type: str) -> str:
        """Determine file extension based on media type."""
        media_type = media_type.lower()
        if media_type == "video":
            return ".mp4"
        elif media_type == "image":
            return ".jpg"
        else:
            return ".jpg"

    def _download_media(self, media_items: List[Dict], existing_files: set):
        """Download all media items."""
        for i, item in enumerate(media_items, start=1):
            media_type = item.get("Media Type", "")
            ext = self._get_file_extension(media_type)
            filename = f"{i:05d}{ext}"

            if filename in existing_files:
                print(f"[SKIP] {filename} (already exists)")
                self.stats["skipped"] += 1
                continue

            url = item.get("Media Download Url")
            if not url:
                print(f"[SKIP] {filename} (no download URL)")
                self.stats["skipped"] += 1
                continue

            self._download_file(url, filename)

    def _download_file(self, url: str, filename: str):
        """Download a single file."""
        filepath = self.output_dir / filename
        print(f"[DOWN] Downloading {filename}...")

        try:
            urllib.request.urlretrieve(url, filepath)
            print(f"[OK]   {filename}")
            self.stats["downloaded"] += 1
        except Exception as e:
            print(f"[FAIL] {filename} - {e}")
            self.stats["failed"] += 1

    def _print_summary(self):
        """Print download summary statistics."""
        print("\n" + "=" * 50)
        print("Download Summary:")
        print(f"  Downloaded: {self.stats['downloaded']}")
        print(f"  Skipped:    {self.stats['skipped']}")
        print(f"  Failed:     {self.stats['failed']}")
        print("=" * 50)


def main():
    """Entry point for the script."""
    json_file = "" #The json file snapchat sent you
    output_dir = ""

    try:
        downloader = SnapchatMemoryDownloader(json_file, output_dir)
        downloader.run()
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
