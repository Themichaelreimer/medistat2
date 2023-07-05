from unittest import TestCase


class TestFunctionTags(TestCase):
    def test_function_tags_generally(self) -> None:
        from function_tags import tag, get_functions_by_tags, get_all_tags
        from typing import Any

        @tag("function", "A", "another_tag")
        def functionA() -> None:
            return None

        @tag("function", "B")
        def functionB(x: Any) -> Any:
            return x

        @tag("function", "C", "another_tag")
        def functionC() -> None:
            return None

        self.assertEqual(get_all_tags(), ["A", "B", "C", "another_tag", "function"])

        self.assertEqual(get_functions_by_tags("A"), {functionA})
        self.assertEqual(get_functions_by_tags("another_tag"), {functionA, functionC})
        self.assertEqual(get_functions_by_tags("A", "B"), {functionA, functionB})

        # B is an identity function. The point of this test is to make sure
        # we can query a function and then call the result of the query
        B_functions = get_functions_by_tags("B")
        self.assertEqual(len(B_functions), 1)
        for fcn in B_functions:
            self.assertEqual(fcn("hi"), "hi")
