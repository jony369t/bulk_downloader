import urllib.request
import urllib.parse
import os
import threading
import time
import sys

# === USER CONFIGURATION ===
url_file = "urls.txt"
save_folder = r"manyDownloads"
max_retries = 3
retry_delay = 3

# === READ URL LIST ===
if not os.path.exists(url_file):
    print(f"❌ URL file '{url_file}' not found. Please create it and add one URL per line.")
    sys.exit(1)

with open(url_file, "r") as f:
    urls = [line.strip() for line in f if line.strip()]

if not urls:
    print("❌ No URLs found in urls.txt.")
    sys.exit(1)

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Shared console lock so threads don't clash
console_lock = threading.Lock()

# Store progress text for each file
progress_lines = [""] * len(urls)

def render_progress():
    """Re-render all progress lines in order."""
    sys.stdout.write("\033[H\033[J")  # clear screen
    for line in progress_lines:
        sys.stdout.write(line + "\n")
    sys.stdout.flush()

def make_progress_callback(index, file_name):
    def progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        percent = downloaded * 100 / total_size if total_size > 0 else 0
        bar_length = 30
        filled = int(bar_length * percent / 100)
        bar = "█" * filled + "-" * (bar_length - filled)

        progress_lines[index] = f"📥 {file_name[:40]:40} | [{bar}] {percent:5.1f}%"
        with console_lock:
            render_progress()
    return progress

def download_file(index, url):
    raw_name = os.path.basename(url.split("?")[0])
    file_name = urllib.parse.unquote(raw_name)
    save_path = os.path.join(save_folder, file_name)

    for attempt in range(1, max_retries + 1):
        try:
            progress_lines[index] = f"⬇️  Starting: {file_name}"
            with console_lock:
                render_progress()

            urllib.request.urlretrieve(
                url,
                save_path,
                make_progress_callback(index, file_name)
            )
            progress_lines[index] = f"✅ Done: {file_name}"
            with console_lock:
                render_progress()
            return
        except Exception as e:
            progress_lines[index] = f"⚠️ Error attempt {attempt} for {file_name}: {e}"
            with console_lock:
                render_progress()
            if attempt < max_retries:
                time.sleep(retry_delay)
            else:
                progress_lines[index] = f"❌ Failed after {max_retries} attempts: {file_name}"
                with console_lock:
                    render_progress()

# Start threads
threads = []
for i, url in enumerate(urls):
    t = threading.Thread(target=download_file, args=(i, url))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n🎉 All downloads attempted. Files are saved in:", save_folder)
input("\nPress Enter to exit...")
