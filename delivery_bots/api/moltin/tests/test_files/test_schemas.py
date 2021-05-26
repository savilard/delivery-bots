import pytest

from delivery_bots.api.moltin.files.schemas import MoltinFile


@pytest.fixture
def moltin_file_response():
    return {
        'data': {
            'type': 'file',
            'id': 'f8cf26b3-6d38-4275-937a-624a83994702',
            'link': {
                'href': 'https://s3-eu-west-1.amazonaws.com/f8cf26b3-6d38-4275-937a-624a83994702.png'
            },
            'file_name': 'f6669358-85db-4367-9cde-1deb77acb5f4.png',
            'mime_type': 'image/png',
            'file_size': 110041,
            'public': True,
            'meta': {
                'dimensions': {
                    'width': 1000,
                    'height': 1000
                },
                'timestamps': {
                    'created_at': '2018-03-13T13:45:21.673Z'
                }
            },
            'links': {
                'self':
                    'https://api.moltin.com/v2/files/f8cf26b3-6d38-4275-937a-624a83994702'
            }
        }
    }


def test_data_section(moltin_file_response):
    moltin_file = MoltinFile(**moltin_file_response).data
    assert moltin_file.type == 'file'
    assert moltin_file.id == 'f8cf26b3-6d38-4275-937a-624a83994702'
    assert moltin_file.file_name == 'f6669358-85db-4367-9cde-1deb77acb5f4.png'
    assert moltin_file.file_size == 110041


def test_link_section(moltin_file_response):
    moltin_file = MoltinFile(**moltin_file_response).data
    assert moltin_file.link.href == 'https://s3-eu-west-1.amazonaws.com/f8cf26b3-6d38-4275-937a-624a83994702.png'


def test_links_section(moltin_file_response):
    moltin_file = MoltinFile(**moltin_file_response).data
    assert moltin_file.links.self == 'https://api.moltin.com/v2/files/f8cf26b3-6d38-4275-937a-624a83994702'


def test_meta_section(moltin_file_response):
    moltin_file = MoltinFile(**moltin_file_response).data
    assert moltin_file.meta.dimensions.height == 1000
    assert moltin_file.meta.timestamps.created_at == '2018-03-13T13:45:21.673Z'
