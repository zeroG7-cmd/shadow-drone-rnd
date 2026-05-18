import os
import sqlite3

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = os.path.join(os.path.dirname(__file__), "../data")

FOLDERS = {
    "hardware": os.path.join(BASE_DIR, "hardware/results"),
    "simulation": os.path.join(BASE_DIR, "simulation/results")
}

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/shadow.db")


# ----------------------------
# Parse log file
# ----------------------------
def parse_file(filepath, source):
    data = {
        "Source": source
    }

    with open(filepath, "r") as f:
        lines = f.readlines()

    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()

    return data


# ----------------------------
# Insert into SQLite
# ----------------------------
def insert_into_db(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name TEXT,
            component TEXT,
            result TEXT,
            notes TEXT,
            time TEXT,
            source TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO test_logs (
            test_name,
            component,
            result,
            notes,
            time,
            source
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data.get("Test"),
        data.get("Component"),
        data.get("Result"),
        data.get("Notes"),
        data.get("Time"),
        data.get("Source")
    ))

    conn.commit()
    conn.close()


# ----------------------------
# Ingest one folder
# ----------------------------
def ingest_folder(folder_path, source_label):
    if not os.path.exists(folder_path):
        print(f"Folder missing: {folder_path}")
        return

    files = os.listdir(folder_path)

    for file in files:
        if file.endswith(".txt") or file.endswith(".md"):
            path = os.path.join(folder_path, file)

            print(f"Ingesting ({source_label}): {file}")

            data = parse_file(path, source_label)
            insert_into_db(data)


# ----------------------------
# Main pipeline
# ----------------------------
def run_ingestion():
    print("\n=== Shadow Robotics Log Ingestion ===\n")

    for source, folder in FOLDERS.items():
        ingest_folder(folder, source)

    print("\nIngestion complete\n")


# ----------------------------
# Run script
# ----------------------------
if __name__ == "__main__":
    run_ingestion()
