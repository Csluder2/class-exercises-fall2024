"""
Run these tests from the CLI (from within the python_rps directory)
as follows:

    python3 run_tests_vanilla.py

"""

from helpers import assert_print, run_all_tests
from your_task import hello_world, rps


def test_hello_world():
    return assert_print(hello_world() == "Hello world!", 'It returns "Hello world!"')


def test_paper_beats_rock():
    return assert_print(
        rps("rock", "paper") == "Paper wins!",  # condition to check
        "Paper beats rock",  # output message
    )


def test_paper_beats_rock_flipped():
    return assert_print(
        rps("paper", "rock") == "Paper wins!",  # condition to check
        "Paper beats rock (flipped)",  # output message
    )


def test_scissor_beats_paper():
    return assert_print(
        rps("paper", "scissor") == "Scissor wins!",  # condition to check
        "Scissor beats paper",  # output message
    )


def test_scissor_beats_paper_flipped():
    return assert_print(
        rps("scissor", "paper") == "Scissor wins!",  # condition to check
        "Scissor beats paper (flipped)",  # output message
    )


def test_rock_beats_scissor():
    return assert_print(
        rps("scissor", "rock") == "Rock wins!",  # condition to check
        "Rock beats scissor",  # output message
    )


def test_rock_beats_scissor_flipped():
    return assert_print(
        rps("rock", "scissor") == "Rock wins!",  # condition to check
        "Rock beats scissor",  # output message
    )


def test_hand1_equals_hand2_rock():
    return assert_print(
        rps("rock", "rock") == "Tie!", "Rock equals rock"  # condition to check
    )


def test_hand1_equals_hand2_paper():
    return assert_print(
        rps("paper", "paper") == "Tie!", "Paper equals paper"  # condition to check
    )


def test_hand1_equals_hand2_scissor():
    return assert_print(
        rps("scissor", "scissor") == "Tie!",  # condition to check
        "Scissor equals scissor",
    )


# don't forget to add any new tests to the list of tests to be run:
run_all_tests(
    [
        test_hello_world,
        test_paper_beats_rock,
        test_paper_beats_rock_flipped,
        test_scissor_beats_paper,
        test_scissor_beats_paper_flipped,
        test_rock_beats_scissor,
        test_rock_beats_scissor_flipped,
        test_hand1_equals_hand2_rock,
        test_hand1_equals_hand2_paper,
        test_hand1_equals_hand2_scissor,
    ]
)
