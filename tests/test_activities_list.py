def test_get_activities_returns_all_expected_fields(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == 9

    for activity_name, activity_details in payload.items():
        assert isinstance(activity_name, str)
        assert expected_fields.issubset(activity_details.keys())
        assert isinstance(activity_details["participants"], list)
