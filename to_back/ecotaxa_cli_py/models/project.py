# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from to_back.ecotaxa_cli_py.configuration import Configuration


class Project(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'projid': 'int',
        'title': 'str',
        'visible': 'bool',
        'status': 'str',
        'mappingobj': 'str',
        'mappingsample': 'str',
        'mappingacq': 'str',
        'mappingprocess': 'str',
        'objcount': 'float',
        'pctvalidated': 'float',
        'pctclassified': 'float',
        'classifsettings': 'str',
        'initclassiflist': 'str',
        'classiffieldlist': 'str',
        'popoverfieldlist': 'str',
        'comments': 'str',
        'projtype': 'str',
        'fileloaded': 'str',
        'rf_models_used': 'str',
        'cnn_network_id': 'str'
    }

    attribute_map = {
        'projid': 'projid',
        'title': 'title',
        'visible': 'visible',
        'status': 'status',
        'mappingobj': 'mappingobj',
        'mappingsample': 'mappingsample',
        'mappingacq': 'mappingacq',
        'mappingprocess': 'mappingprocess',
        'objcount': 'objcount',
        'pctvalidated': 'pctvalidated',
        'pctclassified': 'pctclassified',
        'classifsettings': 'classifsettings',
        'initclassiflist': 'initclassiflist',
        'classiffieldlist': 'classiffieldlist',
        'popoverfieldlist': 'popoverfieldlist',
        'comments': 'comments',
        'projtype': 'projtype',
        'fileloaded': 'fileloaded',
        'rf_models_used': 'rf_models_used',
        'cnn_network_id': 'cnn_network_id'
    }

    def __init__(self, projid=None, title=None, visible=None, status=None, mappingobj=None, mappingsample=None, mappingacq=None, mappingprocess=None, objcount=None, pctvalidated=None, pctclassified=None, classifsettings=None, initclassiflist=None, classiffieldlist=None, popoverfieldlist=None, comments=None, projtype=None, fileloaded=None, rf_models_used=None, cnn_network_id=None, local_vars_configuration=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._projid = None
        self._title = None
        self._visible = None
        self._status = None
        self._mappingobj = None
        self._mappingsample = None
        self._mappingacq = None
        self._mappingprocess = None
        self._objcount = None
        self._pctvalidated = None
        self._pctclassified = None
        self._classifsettings = None
        self._initclassiflist = None
        self._classiffieldlist = None
        self._popoverfieldlist = None
        self._comments = None
        self._projtype = None
        self._fileloaded = None
        self._rf_models_used = None
        self._cnn_network_id = None
        self.discriminator = None

        if projid is not None:
            self.projid = projid
        self.title = title
        if visible is not None:
            self.visible = visible
        if status is not None:
            self.status = status
        if mappingobj is not None:
            self.mappingobj = mappingobj
        if mappingsample is not None:
            self.mappingsample = mappingsample
        if mappingacq is not None:
            self.mappingacq = mappingacq
        if mappingprocess is not None:
            self.mappingprocess = mappingprocess
        if objcount is not None:
            self.objcount = objcount
        if pctvalidated is not None:
            self.pctvalidated = pctvalidated
        if pctclassified is not None:
            self.pctclassified = pctclassified
        if classifsettings is not None:
            self.classifsettings = classifsettings
        if initclassiflist is not None:
            self.initclassiflist = initclassiflist
        if classiffieldlist is not None:
            self.classiffieldlist = classiffieldlist
        if popoverfieldlist is not None:
            self.popoverfieldlist = popoverfieldlist
        if comments is not None:
            self.comments = comments
        if projtype is not None:
            self.projtype = projtype
        if fileloaded is not None:
            self.fileloaded = fileloaded
        if rf_models_used is not None:
            self.rf_models_used = rf_models_used
        if cnn_network_id is not None:
            self.cnn_network_id = cnn_network_id

    @property
    def projid(self):
        """Gets the projid of this Project.  # noqa: E501


        :return: The projid of this Project.  # noqa: E501
        :rtype: int
        """
        return self._projid

    @projid.setter
    def projid(self, projid):
        """Sets the projid of this Project.


        :param projid: The projid of this Project.  # noqa: E501
        :type projid: int
        """

        self._projid = projid

    @property
    def title(self):
        """Gets the title of this Project.  # noqa: E501


        :return: The title of this Project.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Project.


        :param title: The title of this Project.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def visible(self):
        """Gets the visible of this Project.  # noqa: E501


        :return: The visible of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this Project.


        :param visible: The visible of this Project.  # noqa: E501
        :type visible: bool
        """

        self._visible = visible

    @property
    def status(self):
        """Gets the status of this Project.  # noqa: E501


        :return: The status of this Project.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Project.


        :param status: The status of this Project.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def mappingobj(self):
        """Gets the mappingobj of this Project.  # noqa: E501


        :return: The mappingobj of this Project.  # noqa: E501
        :rtype: str
        """
        return self._mappingobj

    @mappingobj.setter
    def mappingobj(self, mappingobj):
        """Sets the mappingobj of this Project.


        :param mappingobj: The mappingobj of this Project.  # noqa: E501
        :type mappingobj: str
        """

        self._mappingobj = mappingobj

    @property
    def mappingsample(self):
        """Gets the mappingsample of this Project.  # noqa: E501


        :return: The mappingsample of this Project.  # noqa: E501
        :rtype: str
        """
        return self._mappingsample

    @mappingsample.setter
    def mappingsample(self, mappingsample):
        """Sets the mappingsample of this Project.


        :param mappingsample: The mappingsample of this Project.  # noqa: E501
        :type mappingsample: str
        """

        self._mappingsample = mappingsample

    @property
    def mappingacq(self):
        """Gets the mappingacq of this Project.  # noqa: E501


        :return: The mappingacq of this Project.  # noqa: E501
        :rtype: str
        """
        return self._mappingacq

    @mappingacq.setter
    def mappingacq(self, mappingacq):
        """Sets the mappingacq of this Project.


        :param mappingacq: The mappingacq of this Project.  # noqa: E501
        :type mappingacq: str
        """

        self._mappingacq = mappingacq

    @property
    def mappingprocess(self):
        """Gets the mappingprocess of this Project.  # noqa: E501


        :return: The mappingprocess of this Project.  # noqa: E501
        :rtype: str
        """
        return self._mappingprocess

    @mappingprocess.setter
    def mappingprocess(self, mappingprocess):
        """Sets the mappingprocess of this Project.


        :param mappingprocess: The mappingprocess of this Project.  # noqa: E501
        :type mappingprocess: str
        """

        self._mappingprocess = mappingprocess

    @property
    def objcount(self):
        """Gets the objcount of this Project.  # noqa: E501


        :return: The objcount of this Project.  # noqa: E501
        :rtype: float
        """
        return self._objcount

    @objcount.setter
    def objcount(self, objcount):
        """Sets the objcount of this Project.


        :param objcount: The objcount of this Project.  # noqa: E501
        :type objcount: float
        """

        self._objcount = objcount

    @property
    def pctvalidated(self):
        """Gets the pctvalidated of this Project.  # noqa: E501


        :return: The pctvalidated of this Project.  # noqa: E501
        :rtype: float
        """
        return self._pctvalidated

    @pctvalidated.setter
    def pctvalidated(self, pctvalidated):
        """Sets the pctvalidated of this Project.


        :param pctvalidated: The pctvalidated of this Project.  # noqa: E501
        :type pctvalidated: float
        """

        self._pctvalidated = pctvalidated

    @property
    def pctclassified(self):
        """Gets the pctclassified of this Project.  # noqa: E501


        :return: The pctclassified of this Project.  # noqa: E501
        :rtype: float
        """
        return self._pctclassified

    @pctclassified.setter
    def pctclassified(self, pctclassified):
        """Sets the pctclassified of this Project.


        :param pctclassified: The pctclassified of this Project.  # noqa: E501
        :type pctclassified: float
        """

        self._pctclassified = pctclassified

    @property
    def classifsettings(self):
        """Gets the classifsettings of this Project.  # noqa: E501


        :return: The classifsettings of this Project.  # noqa: E501
        :rtype: str
        """
        return self._classifsettings

    @classifsettings.setter
    def classifsettings(self, classifsettings):
        """Sets the classifsettings of this Project.


        :param classifsettings: The classifsettings of this Project.  # noqa: E501
        :type classifsettings: str
        """

        self._classifsettings = classifsettings

    @property
    def initclassiflist(self):
        """Gets the initclassiflist of this Project.  # noqa: E501


        :return: The initclassiflist of this Project.  # noqa: E501
        :rtype: str
        """
        return self._initclassiflist

    @initclassiflist.setter
    def initclassiflist(self, initclassiflist):
        """Sets the initclassiflist of this Project.


        :param initclassiflist: The initclassiflist of this Project.  # noqa: E501
        :type initclassiflist: str
        """

        self._initclassiflist = initclassiflist

    @property
    def classiffieldlist(self):
        """Gets the classiffieldlist of this Project.  # noqa: E501


        :return: The classiffieldlist of this Project.  # noqa: E501
        :rtype: str
        """
        return self._classiffieldlist

    @classiffieldlist.setter
    def classiffieldlist(self, classiffieldlist):
        """Sets the classiffieldlist of this Project.


        :param classiffieldlist: The classiffieldlist of this Project.  # noqa: E501
        :type classiffieldlist: str
        """

        self._classiffieldlist = classiffieldlist

    @property
    def popoverfieldlist(self):
        """Gets the popoverfieldlist of this Project.  # noqa: E501


        :return: The popoverfieldlist of this Project.  # noqa: E501
        :rtype: str
        """
        return self._popoverfieldlist

    @popoverfieldlist.setter
    def popoverfieldlist(self, popoverfieldlist):
        """Sets the popoverfieldlist of this Project.


        :param popoverfieldlist: The popoverfieldlist of this Project.  # noqa: E501
        :type popoverfieldlist: str
        """

        self._popoverfieldlist = popoverfieldlist

    @property
    def comments(self):
        """Gets the comments of this Project.  # noqa: E501


        :return: The comments of this Project.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Project.


        :param comments: The comments of this Project.  # noqa: E501
        :type comments: str
        """

        self._comments = comments

    @property
    def projtype(self):
        """Gets the projtype of this Project.  # noqa: E501


        :return: The projtype of this Project.  # noqa: E501
        :rtype: str
        """
        return self._projtype

    @projtype.setter
    def projtype(self, projtype):
        """Sets the projtype of this Project.


        :param projtype: The projtype of this Project.  # noqa: E501
        :type projtype: str
        """

        self._projtype = projtype

    @property
    def fileloaded(self):
        """Gets the fileloaded of this Project.  # noqa: E501


        :return: The fileloaded of this Project.  # noqa: E501
        :rtype: str
        """
        return self._fileloaded

    @fileloaded.setter
    def fileloaded(self, fileloaded):
        """Sets the fileloaded of this Project.


        :param fileloaded: The fileloaded of this Project.  # noqa: E501
        :type fileloaded: str
        """

        self._fileloaded = fileloaded

    @property
    def rf_models_used(self):
        """Gets the rf_models_used of this Project.  # noqa: E501


        :return: The rf_models_used of this Project.  # noqa: E501
        :rtype: str
        """
        return self._rf_models_used

    @rf_models_used.setter
    def rf_models_used(self, rf_models_used):
        """Sets the rf_models_used of this Project.


        :param rf_models_used: The rf_models_used of this Project.  # noqa: E501
        :type rf_models_used: str
        """

        self._rf_models_used = rf_models_used

    @property
    def cnn_network_id(self):
        """Gets the cnn_network_id of this Project.  # noqa: E501


        :return: The cnn_network_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._cnn_network_id

    @cnn_network_id.setter
    def cnn_network_id(self, cnn_network_id):
        """Sets the cnn_network_id of this Project.


        :param cnn_network_id: The cnn_network_id of this Project.  # noqa: E501
        :type cnn_network_id: str
        """

        self._cnn_network_id = cnn_network_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
