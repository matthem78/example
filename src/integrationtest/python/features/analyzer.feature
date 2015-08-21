Feature: host metrics analyzer

  Scenario: Compute stats for each host

    Given a host metric file
    When I analyze the file
    Then I will get the computed min, max, and avg for each host

  Scenario: Host printed in descending order by average
    Given a host metric file
    When I analyze the file
    Then I will see the analyzed metrics in descending order by average
