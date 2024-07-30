# This script is used to setup the platformio environment for the MotorGo boards. This script is a temporary solution until the MotorGo boards are added to the platformio platform.

import os
import sys
import shutil
import glob

# Global variables
# Path to PIO files
PIO_PATH = "~/.platformio"
RELATIVE_PLATFORM_PATH = "platforms"
RELATIVE_PACKAGES_PATH = "packages"

BOARDS_TXT_PATH = "./platformio_board_defs/boards.txt"
BOARD_JSON_PATH = "./platformio_board_defs/board_json/*"
VARIANTS_PATH = "./motorgo_1.0/variants/*"

def copy_package_files(package_versioned_path):
    # Path for package variants
    variants_path = os.path.join(package_versioned_path, "variants")

    # Copy boards.txt with backup
    shutil.copy(os.path.join(package_versioned_path, "boards.txt"), os.path.join(package_versioned_path, "boards.txt.bak"))
    shutil.copy(BOARDS_TXT_PATH, os.path.join(package_versioned_path, "boards.txt"))

    # Copy variants
    for variant in glob.glob(VARIANTS_PATH):
        shutil.copytree(variant, os.path.join(variants_path, os.path.basename(variant)), dirs_exist_ok=True)

def copy_platform_files(platform_versioned_path):
    # Path for platform boards
    boards_path = os.path.join(platform_versioned_path, "boards")

    # Copy board json files
    for json_file in glob.glob(BOARD_JSON_PATH):
        shutil.copy(json_file, os.path.join(boards_path, os.path.basename(json_file)))

def main():
    pio_path = os.path.expanduser(PIO_PATH)
    print("PlatformIO path: " + pio_path)
    print("Copying...")

    # Find all platform versions
    platform_versions = glob.glob(os.path.join(pio_path, RELATIVE_PLATFORM_PATH, "espressif32*"))
    package_versions = glob.glob(os.path.join(pio_path, RELATIVE_PACKAGES_PATH, "framework-arduinoespressif32*"))

    # Run the setup for all package versions
    for package_version in package_versions:
        print(f"Running installer for Package: {os.path.basename(package_version)}")
        copy_package_files(package_version)

    # Run the setup for all platform versions
    for platform_version in platform_versions:
        print(f"Running installer for Platform: {os.path.basename(platform_version)}")
        copy_platform_files(platform_version)

    print("Done!")

if __name__ == "__main__":
    main()