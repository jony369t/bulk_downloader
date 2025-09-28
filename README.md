# Bulk File Downloader (Python)

A simple multithreaded downloader script that can download many files (mkv, mp4, mp3, etc.) at once.  
Supports Windows, Linux, and Android (Termux).

## 🚀 Features
- Download multiple files simultaneously (multithreaded).
- Automatic retry on failed downloads.
- Progress bar with percentage.
- Supports `mkv`, `mp4`, `mp3`, or any direct file link.
- Saves files to your chosen folder (e.g., `D:\manyDownloads`).

## 📦 Installation
1. Install Python (3.7+ recommended)  
   [Download Python](https://www.python.org/downloads/)
2. Clone this repository:
   ```bash
   git clone https://github.com/jony369t/bulk-downloader.git
   cd bulk-downloader
3. Add your file URLs to urls.txt (one per line).

## ▶️ Usage

Run the script with:

```bash
python downloader.py
```
Files will be saved in the folder you configured in the script (default: manyDownloads).

## 📂 Example urls.txt
```
https://example.com/video1.mkv
https://example.com/video2.mp4
https://example.com/audio.mp3
```
## 🖼 Screenshot

<img width="590" height="149" alt="image" src="https://github.com/user-attachments/assets/dc6137b5-e38a-4f57-80c6-d816bb5445ad" />


##💡 Notes

Works on Windows PowerShell, CMD, Linux terminal, and Termux.

If a file fails, the script will retry up to 3 times.
