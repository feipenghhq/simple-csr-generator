#!/usr/bin/python
#########################################################################################
# Copyright 2020 by Heqing Huang (heqinghuangusc@gmail.com)
#
# Project: Simple CSR Generator
# Author: Heqing Huang
# Created: 10/22/2020
#
# Description:
#   This script takes the result from YmlParser and write a HTML documentation
#
#########################################################################################

from common import *

# Define the index for each register
REGNAME = 0
ADDR    = 1
FLDLIST = 2

# Define the index for each field Array
# [Name, MSb, LSb, SWTYPE, HWTYPE, Reset Value, Description]
FNAME   = 0
MSB     = 1
LSB     = 2
SWTYPE  = 3
HWTYPE  = 4
RESET   = 5
NOTE    = 6

class HtmlWriter(object):

    def __init__(self, regsInfo, name, path):
        """
        Parameters:
            :param regsInfo: the register info array for all register
            :param name: the name of the register module
            :param path: the path of to the document
        """
        self.regsInfo = regsInfo
        self.name = name
        self.path = path

    def htmlPrefix(self, FILE, name):
        """
        Write the header par of the HTML file
        Parameters:
            :param name: the name of the register module
            :param FILE: The file pointer
        """
        string  = '<!DOCTYPE html>\n'
        string += '<html lang="">\n'
        string += INDENT(1) + '<head>\n'
        string += INDENT(2) + f'<title>Register module for {name}</title>\n'
        string += INDENT(1) + '</head>\n\n'
        string += INDENT(1) + '<body>\n'
        string += INDENT(2) + '<p>\n'
        string += INDENT(2) + f'CSR Document for {name}<br />\n'
        string += INDENT(2) + 'Generated by Simple CSR Generator<br />\n'
        string += INDENT(2) + f'Created: {MONTH}/{DAY}/{YEAR} {HOUR}:{MINUTE}<br />\n'
        string += INDENT(2) + '</p>\n\n'
        FILE.write(string)

    def htmlsuffix(self, FILE):
        """
        Write the tail par of the HTML file
        Parameters:
            :param name: the name of the register module
            :param FILE: The file pointer
        """
        string  = INDENT(1) + '</head>\n'
        string += '</html>\n'
        FILE.write(string)

    def tableHeader(self, name, addr):
        """
        Write the header for a table
        Parameters:
            :param name: the name of the register
        """
        string  = INDENT(2) + f'<h4>{name}: {addr}</h4>\n'
        string += INDENT(2) + '<table border="4">\n'
        string += INDENT(2) + '<tr>\n'
        string += INDENT(3) + '<td>Field</td>\n'
        string += INDENT(3) + '<td>Range</td>\n'
        string += INDENT(3) + '<td>Reset Value</td>\n'
        string += INDENT(3) + '<td>SW Access Type</td>\n'
        string += INDENT(3) + '<td>HW Access Type</td>\n'
        string += INDENT(3) + '<td>Description</td>\n'
        string += INDENT(2) + '</tr>\n'
        return string

    def OneFieldStr(self, fieldInfo) -> str:
        """
            Write HTML for one field.
            Returns a string of the content to be written

            Parameters:
                :param regInfo: the register info array for 1 register
        """
        string  = INDENT(2) + '<tr>\n'
        string += INDENT(3) + f'<td>{fieldInfo[FNAME]}</td>\n'
        string += INDENT(3) + f'<td>{fieldInfo[MSB]} - {fieldInfo[LSB]}</td>\n'
        string += INDENT(3) + f'<td>{hex(fieldInfo[RESET])}</td>\n'
        string += INDENT(3) + f'<td>{fieldInfo[SWTYPE]}</td>\n'
        string += INDENT(3) + f'<td>{fieldInfo[HWTYPE]}</td>\n'
        string += INDENT(3) + f'<td>{fieldInfo[NOTE]}</td>\n'
        string += INDENT(2) + '</tr>\n'
        return string

    def OneRegStr(self, regInfo):
        """
            Write HTML for one register.
            Returns a string of the content to be written

            Parameters:
                :param regInfo: the register info array for 1 register
        """
        string = self.tableHeader(regInfo[REGNAME], hex(regInfo[ADDR]))
        for fieldInfo in regInfo[FLDLIST]:
            string += self.OneFieldStr(fieldInfo)
        string += INDENT(2) + '</table>\n\n' # table tail
        return string

    def writeAllReg(self, FILE, regsInfo):
        """
            Write all the register.
            Parameters:
                :param FILE: The file pointer
                :param regsInfo: the register info array for all the register
        """
        for regInfo in regsInfo:
            FILE.write(self.OneRegStr(regInfo))

    def writeHtml(self):
        """
            Write all the content.
        """
        fullpath = self.path + '/' + self.name + '_csr.html'
        FILE = open(fullpath, "w")
        self.htmlPrefix(FILE, self.name)
        self.writeAllReg(FILE, self.regsInfo)
        self.htmlsuffix(FILE)
        FILE.close()


if __name__ == "__main__":
    regsInfo = [['pio_read', 0, ['data', 31, 0, 'R', 'W', 0, 'pio read data']], ['pio_write', 4, ['data', 31, 0, 'W', 'R', 0, 'pio write data']], ['pio_ctrl_status', 8, ['edge_capture_en', 0, 0, 'W', 'R', 0, 'enable edge capturing'], ['RSVR', 1, 1, 'NA', 'NA', 0, 'Reserved Field'], ['edge_captured', 2, 2, 'R', 'W', 0, 'captured edge activity (if any)'], ['RSVR', 31, 3, 'NA', 'NA', 0, 'Reserved Field']]]
    path = '.'
    name = 'pio'

    hwriter = HtmlWriter(regsInfo, name, path)
    hwriter.writeHtml()
