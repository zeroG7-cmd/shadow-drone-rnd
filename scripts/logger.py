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
SCRIPTS_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(SCRIPTS_DIR)

DB_PATH = os.path.join(
  BASE_DIR, 
  "database", 
  "shadow.db"
)

DATA_DIR = os.path.join(BASE_DIR, "data")

SIM_RESULTS_DIR = os.path.join(
  DATA_DIR,
  "simulation",
  "results"
)

HARDWARE_RESULTS_DIR = os.path.join(
  DATA_DIR,
  "hardware",
  "result"
)

# -----------------------------
# Runtime Arguments / Inputs
# -----------------------------



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

  
