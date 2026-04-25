# 📷 Automated Machine Vision Data Logger

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![EasyOCR](https://img.shields.io/badge/EasyOCR-Active-brightgreen)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Logging-orange)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

An end-to-end computer vision pipeline designed to bridge the gap between physical machine outputs and digital databases. This tool utilizes Optical Character Recognition (OCR) to automatically extract 16 distinct alphanumeric readings from raw photographs and log them into a structured Excel database with precise timestamps.

Built to eliminate manual data entry bottlenecks in mechanical and manufacturing environments, ensuring high-fidelity data capture for downstream automation.

---

## 🏗️ System Architecture

The pipeline operates on a continuous monitoring loop, processing data from the physical environment to the digital ledger seamlessly:

1. **Capture:** Operator takes a photo of the machine display via smartphone.
2. **Cloud Sync:** Image is automatically synchronized to the local workstation via Google Drive.
3. **Event Detection:** `auto_reader.py` detects the new file in the `/photos` directory.
4. **Vision Processing:** PyTorch-powered EasyOCR extracts all raw text from the image.
5. **Data Parsing:** Custom logic filters and isolates the 16 target variables (`01K` through `16K`).
6. **Database Write:** Data is appended to `machine_readings.xlsx` alongside an execution timestamp, missing value count, and the original image filename.

---

## ⚙️ Prerequisites

Before you begin, ensure you have met the following requirements:
* **OS:** Windows / macOS / Linux
* **Python:** Version 3.8 or higher
* **Hardware:** A CUDA-enabled GPU is highly recommended to accelerate PyTorch/EasyOCR processing, though it will run successfully on a CPU.

---

## 🛠️ Installation & Setup

**1. Clone the repository**
bash
git clone [https://github.com/YourUsername/YourRepositoryName.git](https://github.com/YourUsername/YourRepositoryName.git)
cd YourRepositoryName
2. Create a Virtual Environment (Recommended)
Isolating your dependencies ensures this script doesn't conflict with other Python projects on your machine.

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies

Bash
pip install -r requirement.txt
🚀 Usage
To start the automated logging server, run the main script from your terminal:

Bash
python auto_reader.py
Expected Output:
The terminal will display Waiting for photos....
When a new .jpeg or .png is dropped into the photos/ folder, the terminal will log:

The detected image name.

The raw OCR text output.

The cleaned and parsed variables.

A success message (Saved to Excel!).

📊 Data Structure
The output machine_readings.xlsx generates the following schema automatically:

Date	Time	01K	...	16K	Missing Count	Raw OCR Text	Image Name
YYYY-MM-DD	HH:MM:SS	Float	...	Float	Int	String	String
Note: The Missing Count column acts as an automated quality control check. If a photo is blurry and the OCR misses a parameter, this column flags it for manual review.

🧪 Testing & Calibration
If you need to test the OCR accuracy on a specific image without running the continuous loop, use the test script:

Bash
python test_ocr.py
This is useful for calibrating the OCR confidence thresholds or adjusting for different lighting conditions in the factory/lab.

🗺️ Future Roadmap
[ ] Database Integration: Migrate from Excel to an SQLite or PostgreSQL database for more robust querying.

[ ] Data Visualization: Build a lightweight Streamlit dashboard to visualize the machine readings in real-time.

[ ] Alerting System: Add an email/Discord webhook alert if a captured reading falls outside of safe mechanical tolerances.

👤 Author
Shivam Singh

Mechanical Design Engineer transitioning into Robotics Software Engineering.

Focused on building Python-based automation tools to optimize physical engineering workflows.

LinkedIn Profile
