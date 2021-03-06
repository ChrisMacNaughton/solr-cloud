#!/usr/bin/python

from charmhelpers.core.services.base import ServiceManager
from charmhelpers.core.services import helpers

import actions


def manage():
    manager = ServiceManager([
        {
            'service': 'solr',
            'ports': [8983],  # ports to after start
            'provided_data': [
                # context managers for provided relations
                # e.g.: helpers.HttpRelation()
                helpers.HttpRelation()
            ],
            'required_data': [
                # data (contexts) required to start the service
                # e.g.: helpers.RequiredConfig('domain', 'auth_key'),
                #       helpers.MysqlRelation(),
                helpers.RelationContext('zookeeper', ['private-address','port'])
            ],
            'data_ready': [
                actions.configure_solr,
                actions.log_start,
            ],
        },
    ])
    manager.manage()
