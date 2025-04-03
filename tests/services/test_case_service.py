import pytest
from unittest.mock import Mock
from src.services.case_service import CaseService
from src.models.case import Case
from tests.fixtures import Fixture


@pytest.fixture
def case_repository():
    return Mock()


@pytest.fixture
def case_service(case_repository):
    return CaseService(case_repository)


def test_should_return_all_cases(case_service, case_repository):
    case_repository.get_all_active_cases.return_value = [
        Case(id=Fixture.UUID1),
        Case(id=Fixture.UUID2),
    ]

    cases = case_service.get_all_active_cases()

    assert len(cases) == 2
    case_repository.get_all_active_cases.assert_called_once()


def test_should_return_case_by_id(case_service, case_repository):
    case = Case(id=Fixture.UUID1)
    case_repository.get_case_by_id.return_value = case

    result = case_service.get_case_by_id(Fixture.UUID1)

    assert result == case
    case_repository.get_case_by_id.assert_called_once_with(Fixture.UUID1)


def test_should_create_case(case_service, case_repository):
    case_repository.save_case.return_value = Case(id=Fixture.UUID1, name="Test Case")

    case = case_service.create_case(Case(name="Test Case"))

    assert case.name == "Test Case"
    case_repository.save_case.assert_called_once()


def test_should_update_case_name(case_service, case_repository):
    case_id = Fixture.UUID1
    new_name = "Updated Case Name"
    updated_case = Case(id=case_id, name=new_name)
    case_repository.update_name.return_value = updated_case

    result = case_service.update_case_name(case_id, new_name)

    assert result.name == new_name
    case_repository.update_name.assert_called_once_with(case_id, new_name)


def test_should_delete_case(case_service, case_repository):
    case_repository.delete_case.return_value = True

    result = case_service.delete_case(Fixture.UUID1)

    assert result is True
    case_repository.delete_case.assert_called_once_with(Fixture.UUID1)
