# Automated OCR Machine Data Logger 📷 ➡️ 📊

An end-to-end Python automation pipeline that extracts physical machine readings from photos using Computer Vision (EasyOCR) and logs them directly into an Excel spreadsheet with precise timestamps.

This project was built to eliminate the manual data entry bottleneck in mechanical engineering workflows, bridging the gap between physical hardware readings and digital data processing.

## 🚀 Features

* **Automated Image Processing:** Automatically detects new photos added to a designated folder.
* **Optical Character Recognition (OCR):** Uses EasyOCR and PyTorch to extract complex alphanumeric data from raw images.
* **Intelligent Parsing:** Specifically targets and extracts 16 distinct data points (`01K` through `16K`).
* **Timestamped Logging:** Appends the extracted data, missing value counts, and raw OCR text directly to an Excel file (`machine_readings.xlsx`) with exact date and time logs.
* **Seamless Workflow:** Integrates with Google Drive sync to allow remote data capture via a smartphone camera.

## 🔄 The Workflow

1. **📱 Phone Camera:** Snap a photo of the machine display/readings.
2. **☁️ Google Drive Sync:** The image automatically syncs to your PC via Google Drive.
3. **📁 Local "photos" Folder:** The image lands in the designated local directory.
4. **🧠 Python (EasyOCR):** The `auto_reader.py` script detects the new image and runs OCR.
5. **📊 Excel Log:** Data is cleaned, structured, and saved into the Excel tracking sheet.

## 📂 Project Structure

```text
├── photos/                  # Directory where synced images are dropped
├── .gitignore               # Ignores unwanted files and virtual environments
├── auto_reader.py           # Main automation script for continuous monitoring and OCR
├── machine_readings.xlsx    # Excel database where all readings are logged
├── requirement.txt          # Python dependencies (EasyOCR, pandas, etc.)
├── test_ocr.py              # Script used for testing and tuning the OCR model
🛠️ Setup & Installation
1. Clone the repository:

Bash
git clone [https://github.com/YourUsername/YourRepositoryName.git](https://github.com/YourUsername/YourRepositoryName.git)
cd YourRepositoryName
2. Install dependencies:
Make sure you have Python installed. Install the required libraries using:

Bash
pip install -r requirement.txt
(Note: This project utilizes EasyOCR, which may require PyTorch. If you encounter warning messages regarding GPU acceleration, ensure your PyTorch installation matches your system's CUDA capabilities, or it will default to CPU).

3. Run the automation script:

Bash
python auto_reader.py
The terminal will display Waiting for photos.... As soon as a new image is dropped into the photos/ folder, the script will process it and update the Excel file.

💡 Motivation
As a Mechanical Design Engineer transitioning into software and automation, I built this tool to solve a real-world problem: tedious manual data logging. This project serves as a practical application of Python for mechanical automation, reducing human error and freeing up time for actual engineering analysis.

🤝 Contributing
Feedback, issues, and pull requests are welcome! If you have suggestions for improving OCR accuracy or optimizing the data pipeline, feel free to open an issue.
