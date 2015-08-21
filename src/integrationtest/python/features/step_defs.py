# -*- coding: utf-8 -*-
from lettuce import *
from hamcrest import *
import analyzer

TEST_DATA_FILE = '../../../target/data.txt'

test_host_metrics = [
  'hostA,1366829460,1366831260,60|37.0,65.0,87.0',
  'hostB,1366829460,1366831260,60|None,None,100.0,100.0,99.0,99.0'
]

@step(u'Given a host metric file')
def given_a_host_metric_file(step):
  world.data_file = open(TEST_DATA_FILE, 'w')
  for item in test_host_metrics:
    world.data_file.write("%s\n" % item)

@step(u'When I analyze the file')
def when_i_analyze_the_file(step):
  analyzer.process(world.data_file)  

@step(u'Then I will get the computed min, max, and avg for each host')
def then_i_will_get_the_computed_min_max_and_avg_for_each_host(step):
  assert False, 'This step must be implemented'
