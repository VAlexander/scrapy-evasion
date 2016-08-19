# -*- coding: utf-8 -*-
import datetime

from scrapy import signals
from scrapy.exporters import CsvItemExporter


class CsvExporterPipeline(object):
    # Initialize files
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    # When spider opened, prepare csv exporter
    def spider_opened(self, spider):
        self.number = 0

        file = open('{0:%d-%m-Y_%H-%M}_{1}.csv'.format(datetime.datetime.now(), spider.name), 'w+b')
        self.files['products'] = file
        self.exporter = CsvItemExporter(file)

        self.exporter.fields_to_export = [
            "",
        ]
        self.exporter.encoding = "utf-8"
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    # When spider closed, finish exporting and close the file
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
