"""
A trivial task for health checks
"""


from edx_django_utils.monitoring import set_code_owner_attribute

from openedx.core.lib.celery import APP


@APP.task
@set_code_owner_attribute
def sample_task():
    return True
