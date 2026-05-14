from src.app import activities


def test_signup_adds_new_participant(client, sample_activity_name, sample_email):
    # Arrange
    assert sample_email not in activities[sample_activity_name]["participants"]

    # Act
    response = client.post(
        f"/activities/{sample_activity_name}/signup",
        params={"email": sample_email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {sample_email} for {sample_activity_name}"
    assert sample_email in activities[sample_activity_name]["participants"]


def test_signup_rejects_duplicate_participant(client, sample_activity_name):
    # Arrange
    existing_email = activities[sample_activity_name]["participants"][0]

    # Act
    response = client.post(
        f"/activities/{sample_activity_name}/signup",
        params={"email": existing_email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_signup_rejects_unknown_activity(client, sample_email):
    # Arrange
    unknown_activity = "Unknown Activity"

    # Act
    response = client.post(
        f"/activities/{unknown_activity}/signup",
        params={"email": sample_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
