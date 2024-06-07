import pytest
from src.template_poetry_app.bubble_sort import bubble_sort
from src.template_poetry_app.merge_sort import merge_sort

@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
def test_sort_empty(sort_func):
    arr = []
    sort_func(arr)
    assert arr == []

@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
def test_sort_single_element(sort_func):
    arr = [1]
    sort_func(arr)
    assert arr == [1]

@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
def test_sort_already_sorted(sort_func):
    arr = [1, 2, 3, 4, 5]
    sort_func(arr)
    assert arr == [1, 2, 3, 4, 5]

@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
def test_sort_reverse_sorted(sort_func):
    arr = [5, 4, 3, 2, 1]
    sort_func(arr)
    assert arr == [1, 2, 3, 4, 5]

@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
def test_sort_unsorted(sort_func):
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sort_func(arr)
    assert arr == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

