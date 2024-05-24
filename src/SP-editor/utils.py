import sys
import os
import comtypes.client
import errno

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