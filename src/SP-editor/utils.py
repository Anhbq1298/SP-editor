import sys
import os
import comtypes.client
import errno
import csv
import pandas as pd

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg


def open_url(url):
    qtg.QDesktopServices.openUrl(qtc.QUrl(url))


def about_dialog(parent, title, text):
    qtw.QMessageBox.about(parent, title, text)


def get_save_filename(suffix):
    rv, _ = qtw.QFileDialog.getSaveFileName(caption="Save File", filter='*.{}'.format(suffix))
    if rv != '' and not rv.endswith(suffix): rv += '.' + suffix

    return rv


def get_open_filename(suffix, curr_dir):
    rv, _ = qtw.QFileDialog.getOpenFileName(caption="Open Model File", dir=curr_dir, filter=suffix)
    if rv == '' and not rv.endswith(suffix):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), rv
        )

    return rv


def confirm(parent, title, msg):
    rv = qtw.QMessageBox.question(parent, title, msg, qtw.QMessageBox.Yes, qtw.QMessageBox.No)

    return True if rv == qtw.QMessageBox.Yes else False

def write_to_csv(data, csv_filename):
    """
    Write data to a CSV file.
    
    Args:
        data: The data to be written to the CSV file.
        csv_filename (str): The filename for the CSV file.
    """
    # Write data to CSV
    with open(csv_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

def select_csv_file() -> [str]:
    app = qtw.QApplication(sys.argv)
    dialog = qtw.QFileDialog()
    dialog.setNameFilter("CSV files (*.csv)")
    dialog.setViewMode(dialog.List)
    dialog.setFileMode(dialog.ExistingFile)
    
    if dialog.exec_():
        file_paths = dialog.selectedFiles()
        if file_paths:
            return file_paths[0]  # Return the first selected file path
    return None