class HostMetrics(object):
  hostname = None
  metric_values = []
  average = 0.0
  maximum = 0.0
  minimum = 0.0

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

def process_metrics(metrics_file_path):
  with open(metrics_file_path, 'r') as metrics_file:
    raw_metrics = metrics_file.readlines()

  formatted_metrics = []
  for raw_metric in raw_metrics:
    m = HostMetrics()

    m.hostname = raw_metric.split(',')[0]

    metric_values_as_str = raw_metric.strip().split('|')[1].split(',')
    m.metric_values = [float(metric_value) for metric_value in metric_values_as_str]

    formatted_metrics.append(str(m))

  return formatted_metrics

