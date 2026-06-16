# --------------------------------------------------#
# Shadow Robotics R&D Data Pipeline                 #
#                                                   #
# Author: Sidyfon Afangide                          #
# Alias : Zer0                                      #
#                                                   #
# Project:                                          #
# Shadow Drone R&D Environment                      #
#                                                   #
# Purpose:                                          #
# Logging and managing robotics test data           #
# for simulation and hardware workflows.            #
# --------------------------------------------------#

# -----------------------------#
# Imports                      #
# -----------------------------#
import os
import sqlite3
from datetime import datetime

# -----------------------------#
# Paths / Configuration        #
# -----------------------------#

# Base
SCRIPTS_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(SCRIPTS_DIR)

# Database
DB_PATH = os.path.join(BASE_DIR, "database", "shadow.db") 
                                                                                                                
# Data                                                                                                          
DATA_DIR = os.path.join(BASE_DIR, "data")                 

# Simulation
SIM_BAGS_DIR = os.path.join(DATA_DIR, "simulation", "bags")
SIM_CAMERA_DIR = os.path.join(DATA_DIR, "simulation", "camera")
SIM_LOGS_DIR = os.path.join(DATA_DIR, "simulation", "logs")
SIM_RESULTS_DIR = os.path.join(DATA_DIR, "simulation", "results")

# Hardware
HARDWARE_BAGS_DIR = os.path.join(DATA_DIR, "hardware", "bags")
HARDWARE_CAMERA_DIR = os.path.join(DATA_DIR, "hardware", "camera")
HARDWARE_LOGS_DIR = os.path.join(DATA_DIR, "hardware", "logs")
HARDWARE_RESULTS_DIR = os.path.join(DATA_DIR, "hardware", "results")

# -----------------------------
# Runtime Arguments / Inputs
# -----------------------------

source = input("Please enter source (simulation/hardware): ")

if source not in ["simulation", "hardware"]:
   print("Invalid source. Use 'simulation' or 'hardware'.")
   exit()

print("Selected source:", source)

      
# -----------------------------
# Database Functions
# -----------------------------
def connect_db():
   conn = sqlite3.connect(DB_PATH)
   reture conn

def create_test_logs_table():
   conn = connect_db()
   cursor = conn.cursor()
   
   cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name TEXT,
            component TEXT,
            result TEXT,
            notes TEXT,
            source TEXT,
            timestamp TEXT
        )
    """)  
   conn.commit()
   conn.close()

    

      
def create_telemtry_logs_table():
   conn = connect_db()
   cursor = conn.cursor()

   cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS telemtry_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            battery REAL,
            altitude REAL,
            speed REAL,
            flight_mode TEXT,
            timestamp TEXT
        )
   """) 
   conn.commit()
   conn.close()

  
   
def create_mission_logs_table():
   conn = connect_db()
   cursor = conn.cursor()
   
   cursor.execute("""  
        CREATE TABLE IF NOT EXISTS mission_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mission_name TEXT,
            start_time TEXT,
            end_time TEXT,
            result TEXT,
            notes TEXT
        )
   """) 
   conn.commit()
   conn.close()


def create_perception_logs_table():
   conn = connect_db()
   cursor = conn.cursor()

   cursor.execute("""
        CREATE TABLE IF NOT EXISTS perception_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            object_name TEXT,
            confidence REAL,
            camera_source TEXT,
            timestamp TEXT
        )
   """)
   conn.commit()
   conn.close()


def create_sensor_logs_table():
   conn = connect_db()
   cursor = conn.cursor()

   cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_name TEXT,
            status TEXT,
            value REAL,
            timestamp TEXT
        )
   """)
   conn.commit()
   conn.close()         

def setup_database():
    create_test_logs_table()
    create_telemetry_logs_table()
    create_mission_logs_table()
    create_perception_logs_table()
    create_sensor_logs_table()
   
# -----------------------------
# Logging Functions
# -----------------------------

def log_test(test_name, component, result, notes, source):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")#
   
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
         INSERT INTO test_logs ( 
            test_name,
            component,
            result,
            notes,
            source,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        test_name,
        component,
        result,
        notes,
        source,
        timestamp
    ))

    conn.commit()
    conn.close()

    print("Test logged successfully.")

def log_telemetry(battery, altitude, speed, flight_mode):
   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

   conn = connect_db()
   cursor = conn.cursor()

   cursor.execute("""
         INSERT INTO telemetry_logs (
            battery,
            altitude,
            speed,
            flight_mode,
            timestamp
         )   
           VALUES (?, ?, ?, ?, ?)
    """, (
        battery,
        altitude,
        speed,
        flight_mode,
        timestamp
      ))

    conn.commit()
    conn.close()




def log_mission(mission_name, start_time, end_time, result, notes):
   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")#

   conn = connect_db()
   cursor = conn.cursor()

   cursor.execute("""
         INSERT INTO mission_logs (
            mission_name,
            start_time,
            end_time,
            result,
            notes,
            timestamp
         )   
           VALUES (?, ?, ?, ?, ?, ?)
    """, (
        mission_name,
        start_time,
        end_time,
        result,
        notes,
        timestamp
      ))

    conn.commit()
    conn.close()


def log_perception(object_name, confidence, camera_source):
   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")#

   conn = connect_db()
   cursor = conn.cursor()

   cursor.execute("""
         INSERT INTO perception_logs (
           object_name,
           confidence,
           camera_source,
           timestamp
         )   
           VALUES (?, ?, ?, ?)
    """, (
        object_name,
        confidence,
        camera_source,
        timestamp
      ))

    conn.commit()
    conn.close()


def log_sensor(sensor_name, status, value):
   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")#

   conn = connect_db()
   cursor = conn.cursor()

   cursor.execute("""
         INSERT INTO sensor_logs (
            sensor_name,
            status,
            value,
            timestamp
         )   
           VALUES (?, ?, ?, ?)
    """, (
        sensor_name,
        status,
        value,
        timestamp
      ))

    conn.commit()
    conn.close()
# -----------------------------
# Export Functions
# -----------------------------




# -----------------------------
# Main Runner
# -----------------------------

  
