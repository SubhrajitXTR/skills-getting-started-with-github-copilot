import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def sample_activity_name():
    return "Chess Club"


@pytest.fixture
def sample_email():
    return "student.test@mergington.edu"
