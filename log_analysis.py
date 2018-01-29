#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from logdb import *


class LogAnalysis:
    ''' Class queries and executes the log analyses query string '''
    def __init__(self):
        try:
            self.db = psycopg2.connect('dbname=news')
            self.cursor = self.db.cursor()
        except:
            print("Error in connecting to database")

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def print_analysis(self, report_title, query, ending=" views"):
        result = self.execute_query(query)
        print report_title
        print '_________________________________________________________________'
        for i in range(len(result)):
            print '\t', '*', result[i][0], '--', result[i][1], ending
            print ' '

    def exit(self):
        self.db.close()


if __name__ == '__main__':
    log_analysis = LogAnalysis()
    log_analysis.print_analysis(report_1, query_1)
    log_analysis.print_analysis(report_2, query_2)
    log_analysis.print_analysis(report_3, query_3, " % errors")
    log_analysis.exit()