from src.app import activities


def test_unregister_removes_existing_participant(client, sample_activity_name):
    # Arrange
    registered_email = activities[sample_activity_name]["participants"][0]

    # Act
    response = client.delete(
        f"/activities/{sample_activity_name}/participants",
        params={"email": registered_email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {registered_email} from {sample_activity_name}"
    assert registered_email not in activities[sample_activity_name]["participants"]


def test_unregister_rejects_missing_participant(client, sample_activity_name, sample_email):
    # Arrange
    assert sample_email not in activities[sample_activity_name]["participants"]

    # Act
    response = client.delete(
        f"/activities/{sample_activity_name}/participants",
        params={"email": sample_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"


def test_unregister_rejects_unknown_activity(client, sample_email):
    # Arrange
    unknown_activity = "Unknown Activity"

    # Act
    response = client.delete(
        f"/activities/{unknown_activity}/participants",
        params={"email": sample_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_succeeds_for_email_not_currently_registered(client, sample_activity_name):
    # Arrange
    returning_email = "returning.student@mergington.edu"
    activities[sample_activity_name]["participants"] = [
        email for email in activities[sample_activity_name]["participants"] if email != returning_email
    ]

    # Act
    response = client.post(
        f"/activities/{sample_activity_name}/signup",
        params={"email": returning_email},
    )

    # Assert
    assert response.status_code == 200
    assert returning_email in activities[sample_activity_name]["participants"]
