# -*- coding: utf-8 -*-
from lettuce import *
from hamcrest import *
import analyzer

TEST_HOST_METRICS_FILE_PATH = '../../../target/test_host_metrics.txt'

test_host_metrics = [
  'hostA,1366829460,1366831260,60|37.0,65.0,87.0',
  'hostB,1366829460,1366831260,60|None,None,100.0,100.0,99.0,99.0'
]
analyzed_test_host_metrics = [
  'hostA: Average: 63.0 Max: 87.0 Min: 37.0',
  'hostB: Average: 99.5 Max: 100.0 Min: 99.0'
]

@step(u'Given a host metric file')
def given_a_host_metric_file(step):
  test_host_metrics_file = open(TEST_HOST_METRICS_FILE_PATH, 'w')

  for host_metric in test_host_metrics:
    test_host_metrics_file.write("%s\n" % host_metric)

  test_host_metrics_file.close()

@step(u'When I analyze the file')
def when_i_analyze_the_file(step):
  world.processed_metrics = analyzer.process_metrics(TEST_HOST_METRICS_FILE_PATH)  

@step(u'Then I will get the computed min, max, and avg for each host')
def then_i_will_get_the_computed_min_max_and_avg_for_each_host(step):
  assert_that(world.processed_metrics, has_item(analyzed_test_host_metrics[0]))
  assert_that(world.processed_metrics[1], has_item(analyzed_test_host_metrics[1]))



