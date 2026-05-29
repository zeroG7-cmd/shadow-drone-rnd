# --------------------------------------------------
# Shadow Robotics Logger System
#
# Author: Sidyfon Afangide
# Alias : Zer0
#
# Project:
# Shadow Drone R&D Environment
#
# Purpose:
# Logging and managing robotics test data
# for simulation and hardware workflows.
# --------------------------------------------------

# -----------------------------
# Imports
# -----------------------------
import os
import sqlite3
from datetime import datetime

# -----------------------------
# Paths / Configuration
# -----------------------------

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




# -----------------------------
# Logging Functions
# -----------------------------




# -----------------------------
# Export Functions
# -----------------------------




# -----------------------------
# Main Runner
# -----------------------------

  
