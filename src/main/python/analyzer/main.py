#!/usr/bin/env python
import os.path
from optparse import OptionParser

def process_metrics(metrics_file_path):
  raw_metrics = read_raw_metrics_from_file(metrics_file_path)

  calculated_host_metrics = []
  for raw_metric in raw_metrics:
    tmp_host_metrics = HostMetrics(raw_metric)

    calculated_host_metrics.append(tmp_host_metrics)

  sorted_calculted_host_metrics = sorted(
    calculated_host_metrics,
    key=lambda x: x.average(),
    reverse=True
  )

  return '\n'.join(map(str, sorted_calculted_host_metrics))

def read_raw_metrics_from_file(metrics_file_path):
  with open(metrics_file_path, 'r') as metrics_file:
    raw_metrics = metrics_file.readlines()
  return raw_metrics

class HostMetrics(object):
  hostname = None
  metric_values = []

  def __init__(self, raw_metric):
    self.hostname = raw_metric.split(',')[0]

    metric_values_as_str_arr = raw_metric.strip().split('|')[1].split(',')
    self.metric_values = []
    for metric_value in metric_values_as_str_arr:
      try:
        self.metric_values.append(float(metric_value))
      except ValueError:
        continue

  def average(self):
    return sum(self.metric_values) / float(len(self.metric_values))

  def maximum(self):
    return max(self.metric_values)

  def minimum(self):
    return min(self.metric_values)

  def __str__(self):
    return '%s: Average: %.1f Max: %.1f Min: %.1f' % (
      self.hostname,
      self.average(),
      self.maximum(),
      self.minimum()
    )

def main():
  parser = OptionParser()
  parser.add_option('-f', '--file',
    dest='metrics_file_path',
    default=None)

  (options, args) = parser.parse_args()

  if options.metrics_file_path is None:
    parser.error('Path to metrics file was not given')

  if not os.path.isfile(options.metrics_file_path):
    parser.error('Path provided must be to a valid file')

  print process_metrics(options.metrics_file_path)

if __name__ == '__main__':
  main()