#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_BADGES_MEASURE_ENDPOINT,
    API_PROJECT_BADGES_QUALITY_GATE_ENDPOINT
)


class SonarQubeProjectBadges(RestClient):
    """
    SonarQube project badges Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectBadges, self).__init__(**kwargs)

    def generate_badge_for_project_measures(self, project, metric, branch=None):
        """
        Generate badge for project's measure as an SVG.

        :param project: Project or application key
        :param branch: Long living branch key
        :param metric: Metric key,
          Possible values are for:
            * bugs
            * code_smells
            * coverage
            * duplicated_lines_density
            * ncloc
            * sqale_rating
            * alert_status
            * reliability_rating
            * security_rating
            * sqale_index
            * vulnerabilities
        :return:
        """
        params = {
            'project': project,
            'metric': metric
        }
        if branch:
            params.update({'branch': branch})

        resp = self.get(API_PROJECT_BADGES_MEASURE_ENDPOINT, params=params)
        return resp.text

    def generate_badge_for_project_quality_gate(self, project, branch=None):
        """
        Generate badge for project's quality gate as an SVG.

        :param project: Project or application key
        :param branch: Long living branch key
        :return:
        """
        params = {
            'project': project,
        }
        if branch:
            params.update({'branch': branch})

        resp = self.get(API_PROJECT_BADGES_QUALITY_GATE_ENDPOINT, params=params)
        return resp.text