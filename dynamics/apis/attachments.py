from typing import BinaryIO

from .api_base import ApiBase


class Attachments(ApiBase):
    """Class for Attachments APIs."""

    GET_ATTACHMENTS = '/attachments?$filter=parentId eq {}'
    POST_ATTACHMENT = '/attachments'
    UPLOAD_ATTACHMENT = '/attachments({0})/attachmentContent'

    def get_all(self, parent_id: str):
        """
        Get all attachments
        :return: returns all companies
        """
        return self._get_request({}, Attachments.GET_ATTACHMENTS.format(parent_id))['value']

    def post(self, data):
        """
        Create Attachment
        :param data:
        :return:
        """
        return self._post_request(data, Attachments.POST_ATTACHMENT)

    def upload(self, attachment_id: str, content_type: str, data: BinaryIO):
        """
        Upload attachment to Business Central
        :param parent_id: id of the object the file is to be attached to
        :param attachment_id: id of the attachment object created
        :param content_type: content / mime type of the file
        :param data: Base 64 encoded data
        :return: None
        """
        return self._patch_request(content_type, data, self.UPLOAD_ATTACHMENT.format(attachment_id))
