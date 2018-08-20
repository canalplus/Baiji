#!/usr/bin/python

from generic import Client as GenericClient
from generic import Resource, ResourceCollection

class Client(GenericClient):

    def __init__(self, client, region=None):
        default_version = "2014-05-26"
        default_domain_prefix = 'ecs'
        if region:
            super(Client, self).__init__(
                client, domain_prefix=default_domain_prefix, version=default_version, region=region
            )
        else:
            super(Client, self).__init__(
                client, domain_prefix=default_domain_prefix, version=default_version
            )
        self.__domain = "{}.{}.{}".format(
            self.__domain_prefix,
            self.__region,
            self.__base_domain
        )
        self.instances = Instances(client, self.__domain, self.__version)

class Instances(ResourceCollection):

    def __init__(self, client, domain, version):
        super(Instances, self).__init__(client, domain, version)
        self.__resource_type = "instance"

    def all(self):
        self.create_request("DescribeInstanceStatus")
        response = self.send_request()
        return response

class Instance(Resource):

    def __init__(self, identifier, name):
        super(Instance, self).__init__(identifier, name)
        self.__id = identifier
        self.__name = name
        self.__resource_type = "instance"
