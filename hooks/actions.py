from charmhelpers.core import hookenv


def log_start(service_name):
    hookenv.log('solr starting')

def configure_solr:
    hookenv.log('configuring Solr with Zookeeper')